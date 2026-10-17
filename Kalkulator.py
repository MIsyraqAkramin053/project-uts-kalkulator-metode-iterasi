import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

def hitung():
    try:
        g_str = combo_g.get().strip()
        x0_str = entry_x0.get().strip()
        tol_str = entry_tol.get().strip()
