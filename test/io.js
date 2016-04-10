'use strict';

const basePath = './node_modules/font-awesome/fonts';
const fs = require('fs');
const path = require('path');
const temp = require('temp').track();
const test = require('tap').test;
const woff2 = require('../src/woff2.js');

const magic = {
  ttf: [0x00, 0x01, 0x00, 0x00],
  woff2: [0x77, 0x4f, 0x46, 0x32] // "wOF2"
};

test('Decode WOFF2 data.', (t) => {
  temp.mkdir('node-woff2', (err, dirPath) => {
    if (err) throw err;
    const data =
            fs.readFileSync(path.join(basePath, 'fontawesome-webfont.woff2'));
    const file = path.join(dirPath, 'decoded.ttf');
    // eslint-disable-next-line no-shadow
    fs.writeFile(file, woff2.decode(data), (err) => {
      if (err) throw err;
      fs.open(file, 'r', (err, fd) => { // eslint-disable-line no-shadow
        if (err) throw err;
        const buffer = new Buffer(4);
        // eslint-disable-next-line no-shadow
        fs.read(fd, buffer, 0, 4, 0, (err, bytesRead, buffer) => {
          fs.close(fd, (err) => { // eslint-disable-line no-shadow
            if (err) throw err;
            t.ok(buffer.equals(new Buffer(magic.ttf)));
            t.end();
          });
        });
      });
    });
  });
});

test('Encode WOFF2 data.', (t) => {
  temp.mkdir('node-woff2', (err, dirPath) => {
    if (err) throw err;
    const data =
            fs.readFileSync(path.join(basePath, 'fontawesome-webfont.ttf'));
    const file = path.join(dirPath, 'encoded.woff2');
    // eslint-disable-next-line no-shadow
    fs.writeFile(file, woff2.encode(data), (err) => {
      if (err) throw err;
      fs.open(file, 'r', (err, fd) => { // eslint-disable-line no-shadow
        if (err) throw err;
        const buffer = new Buffer(4);
        // eslint-disable-next-line no-shadow
        fs.read(fd, buffer, 0, 4, 0, (err, bytesRead, buffer) => {
          fs.close(fd, (err) => { // eslint-disable-line no-shadow
            if (err) throw err;
            t.ok(buffer.equals(new Buffer(magic.woff2)));
            t.end();
          });
        });
      });
    });
  });
});
