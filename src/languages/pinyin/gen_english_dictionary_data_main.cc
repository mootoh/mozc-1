// Copyright 2010-2013, Google Inc.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//     * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//     * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#include <string>

#include "base/base.h"
#include "base/codegen_bytearray_stream.h"
#include "base/file_stream.h"
#include "base/logging.h"
#include "base/scoped_ptr.h"
#include "languages/pinyin/english_dictionary_data_builder.h"

DEFINE_string(input, "", "space separated input text files");
DEFINE_string(output, "", "output binary file");

int main(int argc, char **argv) {
  InitGoogle(argv[0], &argc, &argv, false);

  mozc::pinyin::english::EnglishDictionaryDataBuilder builder;
  {
    mozc::InputFileStream ifs(FLAGS_input.c_str());
    builder.BuildFromStream(&ifs);
  }

  scoped_ptr<ostream> output_stream(
      new mozc::OutputFileStream(FLAGS_output.c_str(), ios::out));

  mozc::CodeGenByteArrayOutputStream *codegen_stream;
  output_stream.reset(
      codegen_stream = new mozc::CodeGenByteArrayOutputStream(
          output_stream.release(),
          mozc::codegenstream::OWN_STREAM));
  codegen_stream->OpenVarDef("PinyinEnglishDictionary");

  LOG(INFO) << "Start writing file.";
  builder.WriteToStream(output_stream.get());
  LOG(INFO) << "Start writing file... done.";

  return 0;
}
