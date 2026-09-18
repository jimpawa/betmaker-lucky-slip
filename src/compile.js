const fs = require('fs');
const Babel = require('./assets/3471ce72-fa02-4a51-9b55-c3f6994b7a9a.js');
for (const [src, out] of [
  ['assets/2a98395e-77f7-4722-a958-9bf98a664eb4.js', 'build/components.js'],
  ['build/screens.src.js', 'build/screens.js'],
]) {
  const res = Babel.transform(fs.readFileSync(src, 'utf8'), { presets: ['react'], sourceType: 'script', compact: false });
  fs.writeFileSync(out, res.code);
  console.log(out, res.code.length);
}
