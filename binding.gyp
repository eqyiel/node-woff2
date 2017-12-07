{
  "targets": [
    {
      "target_name": "woff2_encode",
      "sources": ["./src/woff2_encode.cc"],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "./woff2/brotli/c/include",
        "./woff2/include"
      ],
      "cflags": ["-std=c++11 -w"],
      "conditions": [
        [
          "OS!=\"win\"",
          {
            "cflags+": ["-std=c++11"],
            "cflags_c+": ["-std=c++11"],
            "cflags_cc+": ["-std=c++11"]
          }
        ],
        [
          "OS==\"mac\"",
          {
            "xcode_settings": {
              "OTHER_CPLUSPLUSFLAGS": ["-std=c++11", "-stdlib=libc++", "-w"],
              "OTHER_LDFLAGS": ["-stdlib=libc++"],
              "MACOSX_DEPLOYMENT_TARGET": "10.7"
            }
          }
        ]
      ]
    },
    {
      "target_name": "woff2_decode",
      "sources": ["./src/woff2_decode.cc"],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "./woff2/brotli/c/include",
        "./woff2/include",
        "./woff2/src"
      ],
      "cflags": ["-std=c++11 -w"],
      "conditions": [
        [
          "OS!=\"win\"",
          {
            "cflags+": ["-std=c++11"],
            "cflags_c+": ["-std=c++11"],
            "cflags_cc+": ["-std=c++11"]
          }
        ],
        [
          "OS==\"mac\"",
          {
            "xcode_settings": {
              "OTHER_CPLUSPLUSFLAGS": ["-std=c++11", "-stdlib=libc++", "-w"],
              "OTHER_LDFLAGS": ["-stdlib=libc++"],
              "MACOSX_DEPLOYMENT_TARGET": "10.7"
            }
          }
        ]
      ]
    }
  ]
}
