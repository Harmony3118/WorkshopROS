# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import os
import socket
from rclpy.node import Node
from std_msgs.msg import String
from tutorial_interfaces.msg import ComputerInfo

# Constants
COMPUTER = socket.gethostname()[:-2]
ID = int(socket.gethostname()[-1])


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(ComputerInfo, 'topic', 10)
        timer_period = 0.42  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg = ComputerInfo()
        self.msg.counter = 0
        self.msg.computer_name = COMPUTER
        self.msg.domain_id = ID
        self.msg.correct_computer_name = COMPUTER
        self.msg.correct_domain_id = ID
        self.get_logger().info(f'Publishing: {self.msg.computer_name};\t ID: {self.msg.domain_id};\t ')

    def timer_callback(self):
        
        # msg.data = f'Ordi: {COMPUTER};\t ID: {ID};\t Compteur = {self.i}'
        self.publisher_.publish(self.msg)
        self.get_logger().info('Counter: "%d"' % self.msg.counter)
        self.msg.counter += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
