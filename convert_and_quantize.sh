#!/bin/bash

if [ -z $1 ]
then
    echo "You must provide a HF model ID!"
    exit 1
fi

#optimum-cli export onnx -m $1 --optimize O2 models/$1-onnx
optimum-cli onnxruntime quantize --avx512 --onnx_model models/$1-onnx -o models/$1-onnx-quantized
echo "Finished converting to ONNX and quantizing!"
