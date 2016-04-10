#include <string>
#include <nan.h>
#include <node.h>
#include <node_buffer.h>
#include <stdlib.h>
#include "../woff2/src/woff2_dec.h"

using namespace v8;

NAN_METHOD(decode) {
  Local<Object> inputBuffer = info[0]->ToObject();

  if (!node::Buffer::HasInstance(inputBuffer)) {
    Nan::ThrowError(Nan::TypeError("First argument should be a Buffer."));
    return;
  }

  size_t input_length = node::Buffer::Length(inputBuffer);
  char* input_data = node::Buffer::Data(inputBuffer);

  size_t max_output_length = woff2::ComputeWOFF2FinalSize(
    reinterpret_cast<const uint8_t*>(input_data), input_length);
  size_t actual_output_length = max_output_length;

  char* output_data = (char*) calloc(max_output_length, 1);

  if (!woff2::ConvertWOFF2ToTTF(
    reinterpret_cast<uint8_t*>(output_data), actual_output_length,
    reinterpret_cast<const uint8_t*>(input_data), input_length
  )) {
    Nan::ThrowError(Nan::Error("Could not convert the given font."));
    return;
  }

  output_data = (char*) realloc(output_data, actual_output_length);

  Nan::MaybeLocal<v8::Object> outputBuffer = Nan::NewBuffer(
    output_data,
    actual_output_length
  );

  info.GetReturnValue().Set(outputBuffer.ToLocalChecked());
}

NAN_MODULE_INIT(Init) {
  Nan::Set(target, Nan::New("decode").ToLocalChecked(),
    Nan::GetFunction(Nan::New<FunctionTemplate>(decode)).ToLocalChecked());
}

NODE_MODULE(woff2_decode, Init)
