from argparse import ArgumentParser
import cv2
import mediapipe as mp
import numpy as np


#for TCP connection with Unity
import socket
from collections import deque
from playform import system

#face detection and facial landmark
from facial_landmark import FaceMeshDetector

