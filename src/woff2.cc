#include <assert.h>
#include <string.h>
#include "napi.h"
#include <woff2/decode.h>
#include <woff2/encode.h>

static Napi::Value Decode(const Napi::CallbackInfo& info) {
	if (info.Length() != 1) {
		Napi::Error::New(info.Env(), "Expected exactly one argument").ThrowAsJavaScriptException();
		return info.Env().Undefined();
	}

  if (!info[0].IsBuffer()) {
 		Napi::Error::New(info.Env(), "Expected a Buffer").ThrowAsJavaScriptException();
		return info.Env().Undefined();
  }

  Napi::Buffer<char> buf = info[0].As<Napi::Buffer<char>>();

  size_t inputLength = buf.Length();
  char* inputData = reinterpret_cast<char*>(buf.Data());

  size_t outputLength = woff2::ComputeWOFF2FinalSize(
      reinterpret_cast<const uint8_t*>(inputData), inputLength);
  char* outputData = reinterpret_cast<char*>(calloc(outputLength, 1));

  if (!woff2::ConvertWOFF2ToTTF(
          reinterpret_cast<uint8_t*>(outputData), outputLength,
          reinterpret_cast<const uint8_t*>(inputData), inputLength)) {
 		Napi::Error::New(info.Env(), "Could not convert the given font").ThrowAsJavaScriptException();
    free(outputData);
		return info.Env().Undefined();
  }
  Napi::Buffer<char> outputBuf = Napi::Buffer<char>::New(info.Env(), reinterpret_cast<char*>(realloc(outputData, outputLength)), outputLength);
  return outputBuf;
}

static Napi::Value Encode(const Napi::CallbackInfo& info) {
	if (info.Length() != 1) {
		Napi::Error::New(info.Env(), "Expected exactly one argument").ThrowAsJavaScriptException();
		return info.Env().Undefined();
	}

  if (!info[0].IsBuffer()) {
 		Napi::Error::New(info.Env(), "Expected a Buffer").ThrowAsJavaScriptException();
		return info.Env().Undefined();
  }

  Napi::Buffer<char> buf = info[0].As<Napi::Buffer<char>>();

  size_t inputLength = buf.ByteLength();
  char* inputData = reinterpret_cast<char*>(buf.Data());

  size_t outputLength = woff2::MaxWOFF2CompressedSize(
      reinterpret_cast<const uint8_t*>(inputData), inputLength);

  char* outputData = reinterpret_cast<char*>(calloc(outputLength, 1));

  if (!woff2::ConvertTTFToWOFF2(
          reinterpret_cast<const uint8_t*>(inputData), inputLength,
          reinterpret_cast<uint8_t*>(outputData), &outputLength)) {
 		Napi::Error::New(info.Env(), "Could not convert the given font").ThrowAsJavaScriptException();
    free(outputData);
		return info.Env().Undefined();
  }
  Napi::Buffer<char> outputBuf = Napi::Buffer<char>::New(info.Env(), reinterpret_cast<char*>(realloc(outputData, outputLength)), outputLength);
  return outputBuf;
}

static Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports["decode"] = Napi::Function::New(env, Decode);
  exports["encode"] = Napi::Function::New(env, Encode);
  return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
