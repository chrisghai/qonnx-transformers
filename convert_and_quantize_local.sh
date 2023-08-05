#!/bin/bash

if [ -z $1 ]
then
    echo "First argument must be path to local model dir!"
    exit 1
fi

if [ -z $2 ]
then
    echo "Second argument must be a task!"
    exit 1
fi

python convert_to_onnx.py -m $1 -t $2
optimum-cli onnxruntime quantize --avx512 --onnx_model $1-onnx -o $1-onnx-quantized
echo "Finished converting to ONNX and quantizing!"
