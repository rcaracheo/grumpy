from ipykernel.kernelapp import IPKernelApp
from . import GrumpyKernel

IPKernelApp.launch_instance(kernel_class=GrumpyKernel)
