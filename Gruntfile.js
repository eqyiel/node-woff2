'use strict';

const template = `# node-woff2

This is just a Node.js wrapper around Google\'s excellent
[woff2](https://github.com/google/woff2) utility.

## Special thanks

[nfroidure](https://github.com/nfroidure) wrote a wrapper that
converts TTF to WOFF2.  I wanted something that could encode
and decode though, so I recycled his \`bindings.gyp\` file, and
the file \`./src/woff2_encode.cc\` is more or less straight from
his repository.  In respect for his work this wrapper is also
under the MIT license.

## API Reference
{{>all-docs~}}`;

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
          template
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
