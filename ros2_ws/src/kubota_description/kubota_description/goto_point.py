#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
import math

def euler_from_quaternion(x, y, z, w):
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    return math.atan2(t3, t4)

class AckermannGotoPoint(Node):
    def __init__(self):
        super().__init__('ackermann_goto_point')

        # Suscriptores
        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.create_subscription(Point, '/goal_pose', self.goal_callback, 10)

        # Publicador de velocidad
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Timer de control a 20 Hz (0.05s)
        self.create_timer(0.05, self.control_loop)

        # Estado actual
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0

        # Meta (None hasta que llegue el primer mensaje por /goal_pose)
        self.goal_x = None
        self.goal_y = None

        # Ganancias de Control
        self.kp_linear = 0.5
        self.kp_angular = 1.2

        # Límites del Kubota
        self.max_linear_speed = 1.2   # m/s
        self.max_angular_speed = 0.7  # rad/s (aprox 40 deg)
        self.distance_tolerance = 0.25 # Tolerancia de llegada (metros)

        self.get_logger().info('Nodo de Control Ackermann iniciado. Esperando objetivo en /goal_pose...')

    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        self.current_yaw = euler_from_quaternion(q.x, q.y, q.z, q.w)

    def goal_callback(self, msg):
        self.goal_x = msg.x
        self.goal_y = msg.y
        self.get_logger().info(f'Nueva meta recibida -> X: {self.goal_x:.2f}, Y: {self.goal_y:.2f}')

    def control_loop(self):
        if self.goal_x is None or self.goal_y is None:
            return

        dx = self.goal_x - self.current_x
        dy = self.goal_y - self.current_y
        distance_error = math.hypot(dx, dy)

        cmd = Twist()

        # Criterio de LLegada
        if distance_error < self.distance_tolerance:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.cmd_pub.publish(cmd)
            self.get_logger().info('¡Llegada a la meta exitosa!')
            self.goal_x = None
            self.goal_y = None
            return

        # Ángulo objetivo hacia la coordenada
        target_yaw = math.atan2(dy, dx)
        heading_error = math.atan2(math.sin(target_yaw - self.current_yaw), 
                                   math.cos(target_yaw - self.current_yaw))

        # Control Proporcional con límites dinámicos
        # Si el error de orientación es alto (> 60°), desacelera para no desviarse en giros cerrados
        speed_factor = max(0.2, math.cos(heading_error))
        
        linear_val = self.kp_linear * distance_error * speed_factor
        angular_val = self.kp_angular * heading_error

        # Saturación de velocidades según límites físicos
        cmd.linear.x = min(linear_val, self.max_linear_speed)
        cmd.angular.z = max(-self.max_angular_speed, min(angular_val, self.max_angular_speed))

        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = AckermannGotoPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
