from setuptools import find_packages
from setuptools import setup

package_name = 'my_first_ros_rclpy_pkg'

setup(
    name=package_name,
    version='0.0.2',
    #packages=[package_name],
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ola',
    maintainer_email='abrahamola80@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'helloworld_publisher = my_first_ros_rclpy_pkg.helloworld_publisher:main',
            'helloworld_subscriber = my_first_ros_rclpy_pkg.helloworld_subscriber:main',
        ],
    },
)
