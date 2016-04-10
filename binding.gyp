{
  "targets": [
    { "target_name": "woff2_encode",
      "sources": [
        "./src/woff2_encode.cc",
        "./woff2/brotli/enc/backward_references.cc",
        "./woff2/brotli/enc/block_splitter.cc",
        "./woff2/brotli/enc/brotli_bit_stream.cc",
        "./woff2/brotli/enc/encode.cc",
        "./woff2/brotli/enc/encode_parallel.cc",
        "./woff2/brotli/enc/entropy_encode.cc",
        "./woff2/brotli/enc/histogram.cc",
        "./woff2/brotli/enc/literal_cost.cc",
        "./woff2/brotli/enc/metablock.cc",
        "./woff2/brotli/enc/static_dict.cc",
        "./woff2/brotli/enc/streams.cc",
        "./woff2/src/font.cc",
        "./woff2/src/glyph.cc",
        "./woff2/src/normalize.cc",
        "./woff2/src/table_tags.cc",
        "./woff2/src/transform.cc",
        "./woff2/src/variable_length.cc",
        "./woff2/src/woff2_common.cc",
        "./woff2/src/woff2_compress.cc",
        "./woff2/src/woff2_enc.cc"
      ],
      "include_dirs"  : [
        "<!(node -e \"require('nan')\")",
        "./woff2/brotli/enc"
      ],
      "cflags": [
        "-std=c++11 -w"
      ],
      "conditions": [
        [ "OS!=\"win\"", {
          "cflags+": [ "-std=c++11" ],
          "cflags_c+": [ "-std=c++11" ],
          "cflags_cc+": [ "-std=c++11" ]
        }],
        [ "OS==\"mac\"", {
          "xcode_settings": {
            "OTHER_CPLUSPLUSFLAGS": [ "-std=c++11", "-stdlib=libc++", "-w" ],
            "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
            "MACOSX_DEPLOYMENT_TARGET": "10.7"
          }
        }]
      ]
    },
    { "target_name": "woff2_decode",
      "sources": [
        "./src/woff2_decode.cc",
        "./woff2/brotli/dec/bit_reader.c",
        "./woff2/brotli/dec/decode.c",
        "./woff2/brotli/dec/huffman.c",
        "./woff2/brotli/dec/safe_malloc.c",
        "./woff2/brotli/dec/state.c",
        "./woff2/brotli/dec/streams.c",
        "./woff2/src/font.cc",
        "./woff2/src/glyph.cc",
        "./woff2/src/normalize.cc",
        "./woff2/src/table_tags.cc",
        "./woff2/src/transform.cc",
        "./woff2/src/variable_length.cc",
        "./woff2/src/woff2_common.cc",
        "./woff2/src/woff2_dec.cc",
        "./woff2/src/woff2_decompress.cc",
        "./woff2/src/woff2_out.cc"
      ],
      "include_dirs"  : [
        "<!(node -e \"require('nan')\")",
        "./woff2/brotli/dec"
      ],
      "cflags": [
        "-std=c++11 -w"
      ],
      "conditions": [
        [ "OS!=\"win\"", {
          "cflags+": [ "-std=c++11" ],
          "cflags_c+": [ "-std=c++11" ],
          "cflags_cc+": [ "-std=c++11" ]
        }],
        [ "OS==\"mac\"", {
          "xcode_settings": {
            "OTHER_CPLUSPLUSFLAGS": [ "-std=c++11", "-stdlib=libc++", "-w" ],
            "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
            "MACOSX_DEPLOYMENT_TARGET": "10.7"
          }
        }]
      ]
    }]
}
