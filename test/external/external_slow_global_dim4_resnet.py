# ruff: noqa: E501
import os
if "CACHELEVEL" not in os.environ: os.environ["CACHELEVEL"] = "0"

from tinygrad import dtypes, Device
from tinygrad.ops import LazyOp, BinaryOps, UnaryOps, BufferOps, MemBuffer, ConstBuffer
from tinygrad.shape.view import View
from tinygrad.shape.shapetracker import ShapeTracker
from tinygrad.codegen.linearizer import Linearizer
from tinygrad.engine.search import time_linearizer, bufs_from_lin

# from resnet50, tinybox red
# before lowerer 1.13ms on commit 204b6169
# 8.67ms on master 01fbd182
ast = LazyOp(op=BufferOps.STORE, src=(LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=BinaryOps.ADD, src=(LazyOp(op=BinaryOps.ADD, src=(LazyOp(op=BinaryOps.ADD, src=(LazyOp(op=BinaryOps.MUL, src=(LazyOp(op=BinaryOps.ADD, src=(LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=1, dtype=dtypes.half, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(401408, 0, 3136, 56, 1, 0, 0, 0), offset=0, mask=None, contiguous=True),)))),), arg=dtypes.float), LazyOp(op=UnaryOps.NEG, src=(LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=2, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),)))),), arg=None)), arg=None), LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=3, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),))))), arg=None), LazyOp(op=BinaryOps.MUL, src=(LazyOp(op=BinaryOps.ADD, src=(LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=1, dtype=dtypes.half, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(401408, 0, 3136, 56, 1, 0, 0, 0), offset=0, mask=None, contiguous=True),)))),), arg=dtypes.float), LazyOp(op=UnaryOps.NEG, src=(LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=2, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),)))),), arg=None)), arg=None), LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=3, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),))))), arg=None)), arg=None), LazyOp(op=BinaryOps.MUL, src=(LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=4, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),)))), LazyOp(op=BinaryOps.MUL, src=(LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=5, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),)))), LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=BinaryOps.MUL, src=(LazyOp(op=UnaryOps.CAST, src=(LazyOp(op=BinaryOps.CMPLT, src=(LazyOp(op=BufferOps.CONST, src=(), arg=ConstBuffer(val=0.0, dtype=dtypes.half, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 0, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),)))), LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=6, dtype=dtypes.half, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(401408, 0, 3136, 56, 1, 0, 0, 0), offset=0, mask=None, contiguous=True),))))), arg=None),), arg=dtypes.half), LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=7, dtype=dtypes.half, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(430592, 0, 3364, 58, 1, 0, 0, 0), offset=59, mask=None, contiguous=False),))))), arg=None),), arg=dtypes.float)), arg=None)), arg=None)), arg=None), LazyOp(op=BufferOps.LOAD, src=(), arg=MemBuffer(idx=8, dtype=dtypes.float, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(0, 0, 1, 0, 0, 0, 0, 0), offset=0, mask=None, contiguous=False),))))), arg=None),), arg=dtypes.half),), arg=dtypes.float),), arg=dtypes.half),), arg=MemBuffer(idx=0, dtype=dtypes.half, st=ShapeTracker(views=(View(shape=(256, 1, 128, 56, 56, 1, 1, 1), strides=(401408, 0, 3136, 56, 1, 0, 0, 0), offset=0, mask=None, contiguous=True),))))

device = Device[Device.DEFAULT]
rawbufs = bufs_from_lin(Linearizer(ast))

lin = Linearizer(ast, opts=device.renderer)
lin.hand_coded_optimizations()
tm = time_linearizer(lin, rawbufs, allow_test_size=False, cnt=10)
print(f"{tm=}")