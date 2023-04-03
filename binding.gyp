{
  "targets": [
    {
      "target_name": "example",
      "sources": [ "example.c", "example_wrap.cc" ],
      "include_dirs": [ "<!@(node -p \"require('node-addon-api').include\")" ]
    }
  ]
}