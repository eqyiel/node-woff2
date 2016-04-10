'use strict';

module.exports = (grunt) => {
  grunt.initConfig({
    clean: ['./README.md'],
    eslint: {
      target: [
        './src/**/*.js',
        './test/**/*.js'
      ]
    },
    jsdoc2md: {
      withOptions: {
        options: {
          template: '# node-woff2\r\n\r\n' +
            'This is just a Node.js wrapper around Google\'s excellent ' +
            '[woff2](https://github.com/google/woff2) utility.\r\n\r\n' +
            '## Special thanks\r\n\r\n' +
            '[nfroidure](https://github.com/nfroidure) wrote a wrapper that ' +
            'converts TTF to WOFF2.  I wanted something that could encode ' +
            'and decode though, so I recycled his `bindings.gyp` file, and ' +
            'the file `./src/woff2_encode.cc` is more or less straight from ' +
            'his repository.  In respect for his work this wrapper is also ' +
            'under the MIT license.\r\n\r\n' +
            '## API Reference\r\n\r\n{{>all-docs~}}\r\n\r\n***\r\n'
        },
        src: 'src/*.js',
        dest: './README.md'
      }
    },
  });

  grunt.loadNpmTasks('grunt-eslint');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-jsdoc-to-markdown');
  grunt.registerTask('default', [
    'eslint',
    'clean',
    'jsdoc2md'
  ]);
};
