# Copyright 2010-2013, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'variables': {
    'relative_dir': 'languages/pinyin',
    'gen_out_dir': '<(SHARED_INTERMEDIATE_DIR)/<(relative_dir)',
  },
  'targets': [
    {
      # Meta target to set up build environment.
      'target_name': 'pinyin_build_environment',
      'type': 'none',
      'variables': {
        'pinyin_libs': [
          'pyzy-1.0',
        ],
      },
      'all_dependent_settings': {
        'cflags': [
          '<!@(<(pkg_config_command) --cflags <@(pinyin_libs))',
        ],
        'link_settings': {
          'libraries': [
            '<!@(<(pkg_config_command) --libs-only-l <@(pinyin_libs))',
          ],
          'ldflags': [
            '<!@(<(pkg_config_command) --libs-only-L <@(pinyin_libs))',
          ],
        },
      },
    },
    {
      'target_name': 'pinyin_session',
      'type': 'static_library',
      'sources': [
        'session.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
        '../../session/session_base.gyp:session_protocol',
        'pinyin_keymap',
        'pinyin_session_converter',
      ],
    },
    {
      'target_name': 'pinyin_session_factory',
      'type': 'static_library',
      'sources': [
        'pinyin_session_factory.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        # TODO(hsumita): remove a dependency on session_protocol
        '../../session/session_base.gyp:session_protocol',
        'pinyin_session',
      ],
    },
    {
      'target_name': 'pinyin_session_converter',
      'type': 'static_library',
      'sources': [
        'session_converter.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../session/session_base.gyp:key_event_util',
        '../../session/session_base.gyp:session_protocol',
        'pinyin_context',
        'pinyin_direct_context',
        'pinyin_english_context',
        'pinyin_punctuation_context',
      ],
    },
    {
      'target_name': 'pinyin_context',
      'type': 'static_library',
      'sources': [
        'pinyin_context.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
        'pinyin_build_environment',
      ],
    },
    {
      'target_name': 'pinyin_punctuation_context',
      'type': 'static_library',
      'sources': [
        'punctuation_context.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        'pinyin_punctuation_table',
      ],
    },
    {
      'target_name': 'pinyin_direct_context',
      'type': 'static_library',
      'sources': [
        'direct_context.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
      ],
    },
    {
      'target_name': 'pinyin_context_mock',
      'type': 'static_library',
      'sources': [
        'pinyin_context_mock.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
      ],
    },
    {
      'target_name': 'pinyin_keymap',
      'type': 'static_library',
      'sources': [
        'keymap.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
        '../../session/session_base.gyp:key_event_util',
        '../../session/session_base.gyp:session_protocol',
        'pinyin_configurable_keymap',
        'pinyin_default_keymap',
      ],
    },
    {
      'target_name': 'pinyin_configurable_keymap',
      'type': 'static_library',
      'sources': [
        'configurable_keymap.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
        '../../session/session_base.gyp:key_event_util',
        '../../session/session_base.gyp:session_protocol',
      ],
    },
    {
      'target_name': 'pinyin_default_keymap',
      'type': 'static_library',
      'sources': [
        'default_keymap.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../session/session_base.gyp:key_event_util',
        '../../session/session_base.gyp:session_protocol',
      ],
    },
    {
      'target_name': 'pinyin_english_context',
      'type': 'static_library',
      'sources': [
        'english_context.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        'pinyin_english_dictionary_factory',
      ],
    },
    {
      'target_name': 'pinyin_english_dictionary',
      'type': 'static_library',
      'sources': [
        'english_dictionary.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../base/base.gyp:config_file_stream',
        '../../dictionary/file/dictionary_file.gyp:codec',
        '../../dictionary/file/dictionary_file.gyp:dictionary_file',
        '../../storage/louds/louds.gyp:louds_trie',
        '../../storage/storage.gyp:encrypted_string_storage',
        'gen_pinyin_english_dictionary_data#host',
      ],
    },
    {
      'target_name': 'pinyin_english_dictionary_factory',
      'type': 'static_library',
      'sources': [
        'english_dictionary_factory.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        'pinyin_english_dictionary',
      ],
    },
    {
      'target_name': 'pinyin_punctuation_table',
      'type': 'static_library',
      'sources': [
        'punctuation_table.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
      ],
    },
    # test
    {
      # TODO(hsumita): We should add it to gyp/test.gyp.
      'target_name': 'pinyin_all_test',
      'type': 'none',
      'dependencies': [
        'pinyin_configurable_keymap_test',
        'pinyin_context_mock_test',
        'pinyin_context_test',
        'pinyin_default_keymap_test',
        'pinyin_direct_context_test',
        'pinyin_english_context_test',
        'pinyin_english_dictionary_factory_test',
        'pinyin_english_dictionary_test',
        'pinyin_keymap_test',
        'pinyin_punctuation_context_test',
        'pinyin_punctuation_table_test',
        'pinyin_session_converter_test',
        'pinyin_session_factory_test',
        'pinyin_session_test',
      ],
    },
    {
      'target_name': 'pinyin_context_test',
      'type': 'executable',
      'sources': [
        'pinyin_context_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        'pinyin_context',
      ],
    },
    {
      'target_name': 'pinyin_punctuation_context_test',
      'type': 'executable',
      'sources': [
        'punctuation_context_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        'pinyin_punctuation_context',
      ],
    },
    {
      'target_name': 'pinyin_direct_context_test',
      'type': 'executable',
      'sources': [
        'direct_context_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        'pinyin_direct_context',
      ],
    },
    {
      'target_name': 'pinyin_context_mock_test',
      'type': 'executable',
      'sources': [
        'pinyin_context_mock_test.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_context_mock',
      ],
    },
    {
      'target_name': 'pinyin_keymap_test',
      'type': 'executable',
      'sources': [
        'keymap_test.cc',
      ],
      'dependencies': [
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
        '../../session/session_base.gyp:key_parser',
        '../../session/session_base.gyp:session_protocol',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_keymap',
      ],
    },
    {
      'target_name': 'pinyin_configurable_keymap_test',
      'type': 'executable',
      'sources': [
        'configurable_keymap_test.cc',
      ],
      'dependencies': [
        '../../config/config.gyp:config_handler',
        '../../config/config.gyp:config_protocol',
        '../../session/session_base.gyp:key_parser',
        '../../session/session_base.gyp:session_protocol',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_configurable_keymap',
      ],
    },
    {
      'target_name': 'pinyin_default_keymap_test',
      'type': 'executable',
      'sources': [
        'default_keymap_test.cc',
      ],
      'dependencies': [
        '../../session/session_base.gyp:key_parser',
        '../../session/session_base.gyp:session_protocol',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_default_keymap',
      ],
    },
    {
      'target_name': 'pinyin_session_converter_test',
      'type': 'executable',
      'sources': [
        'session_converter_test.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_session_converter',
      ],
    },
    {
      'target_name': 'pinyin_session_factory_test',
      'type': 'executable',
      'sources': [
        'pinyin_session_factory_test.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_session_factory',
      ],
    },
    {
      'target_name': 'pinyin_session_test',
      'type': 'executable',
      'sources': [
        'session_test.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../config/config.gyp:config_handler',
        '../../session/session_base.gyp:key_parser',
        '../../session/session_base.gyp:session_protocol',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_context_mock',
        'pinyin_session',
        'pinyin_session_converter',
      ],
    },
    {
      'target_name': 'pinyin_english_context_test',
      'type': 'executable',
      'sources': [
        'english_context_test.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../testing/testing.gyp:gtest_main',
        'pinyin_english_context',
      ],
    },
    {
      'target_name': 'pinyin_english_dictionary_test',
      'type': 'executable',
      'sources': [
        'english_dictionary_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        'pinyin_english_dictionary',
      ],
    },
    {
      'target_name': 'pinyin_english_dictionary_factory_test',
      'type': 'executable',
      'sources': [
        'english_dictionary_factory_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        'pinyin_english_dictionary_factory',
      ],
    },
    {
      'target_name': 'pinyin_punctuation_table_test',
      'type': 'executable',
      'sources': [
        'punctuation_table_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        'pinyin_punctuation_table'
      ],
    },
    # generates data.
    {
      'target_name': 'gen_pinyin_english_dictionary_data',
      'type': 'none',
      'toolsets': ['host'],
      'actions': [
        {
          'action_name': 'gen_pinyin_english_dictionary_data',
          'variables': {
             'input_file':
               '../../data/pinyin/english_dictionary.txt',
             'output_file':
               '<(gen_out_dir)/pinyin_embedded_english_dictionary_data.h',
          },
          'inputs': [
            '<(input_file)',
          ],
          'outputs': [
            '<(output_file)',
          ],
          'action': [
            '<(mozc_build_tools_dir)/gen_pinyin_english_dictionary_data_main',
            '--logtostderr',
            '--input=<(input_file)',
            '--output=<(output_file)',
          ],
          'message': 'Generating <(output_file).',
        },
      ],
    },
    {
      'target_name': 'pinyin_english_dictionary_data_builder',
      'type': 'static_library',
      'toolsets': ['host'],
      'sources': [
        'english_dictionary_data_builder.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../dictionary/file/dictionary_file.gyp:codec',
        '../../dictionary/file/dictionary_file.gyp:dictionary_file',
        '../../storage/louds/louds.gyp:louds_trie_builder',
      ],
    },
    {
      'target_name': 'gen_pinyin_english_dictionary_data_main',
      'type': 'executable',
      'toolsets': ['host'],
      'sources': [
        'gen_english_dictionary_data_main.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        'pinyin_english_dictionary_data_builder',
      ],
    },
    {
      'target_name': 'install_gen_pinyin_english_dictionary_data_main',
      'type': 'none',
      'toolsets': ['host'],
      'variables': {
        'bin_name': 'gen_pinyin_english_dictionary_data_main'
      },
      'includes' : [
        '../../gyp/install_build_tool.gypi'
      ],
    },
  ],
  # for Linux
  'conditions': [
    ['OS=="linux"', {
      'targets': [
        {
          'target_name': 'ibus_mozc_pinyin',
          'type': 'executable',
          'sources': [
            'unix/ibus/main.cc',
            'unix/ibus/mozc_engine_property.cc',
          ],
          'dependencies': [
            '../../config/config.gyp:config_handler',
            '../../config/config.gyp:config_protocol',
            '../../base/base.gyp:base',
            '../../protobuf/protobuf.gyp:protobuf',
            '../../session/session.gyp:session_handler',
            '../../unix/ibus/ibus.gyp:ibus_mozc_lib',
            'pinyin_session',
          ],
          'conditions': [
            ['target_platform=="ChromeOS"', {
              'sources': [
                'unix/ibus/config_updater.cc',
              ],
              'dependencies': [
                '../../config/config.gyp:config_handler',
                '../../config/config.gyp:config_protocol',
                'pinyin_session_factory',
              ],
            }],
          ],
        },
        {
          'target_name': 'mozc_server_pinyin',
          'type': 'executable',
          'sources': [
            'server_main.cc',
          ],
          'dependencies': [
            '../../server/server.gyp:mozc_server_lib',
            'pinyin_session_factory',
          ],
        },
      ],
    }],
  ],
}
