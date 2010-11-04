// Copyright 2010, Google Inc.
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

#ifndef MOZC_DICTIONARY_USER_DICTIONARY_H_
#define MOZC_DICTIONARY_USER_DICTIONARY_H_

#include <string>
#include <vector>
#include "base/base.h"
#include "base/thread.h"
#include "dictionary/dictionary_interface.h"
#include "dictionary/user_pos.h"

namespace mozc {

class UserDictionaryStorage;
class UserDictionaryReloader;

class UserDictionary : public DictionaryInterface {
 public:
  UserDictionary();
  virtual ~UserDictionary();

  virtual Node *LookupPredictive(const char *str, int size,
                                 NodeAllocatorInterface *allocator) const;
  virtual Node *LookupPrefix(const char *str, int size,
                             NodeAllocatorInterface *allocator) const;
  virtual Node *LookupReverse(const char *str, int size,
                              NodeAllocatorInterface *allocator) const;

  // Load dictionary from UserDictionaryStorage.
  // mainly for unittesting
  bool Load(const UserDictionaryStorage &storage);

  // Reload
  bool Reload();

  // Reload dictionary asynchronously
  bool AsyncReload();

  // Wait until reloader finishes
  void WaitForReloader();

  // Return an singleton object
  static UserDictionary *GetUserDictionary();

  // Set user dicitonary filename for unittesting
  static void SetUserDictionaryName(const string &filename);

 private:
  friend class UserDictionaryTest;

  void Clear();
  bool CheckReloaderAndDelete() const;

  vector<UserPOS::Token *> tokens_;
  mutable scoped_ptr<UserDictionaryReloader> reloader_;
  DISALLOW_COPY_AND_ASSIGN(UserDictionary);
};
}  // namespace mozc

#endif  // MOZC_DICTIONARY_USER_DICTIONARY_H_
