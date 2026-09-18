const fs = require('fs');
const Babel = require('./assets/7dffd603-a9ba-448f-85eb-fc73f43f5f71.js');
for (const [src, out] of [
  ['assets/bf8f3593-177b-4742-809f-eca8b57998d3.js', 'build/components.js'],
  ['build/screens.src.js', 'build/screens.js'],
]) {
  const res = Babel.transform(fs.readFileSync(src, 'utf8'), { presets: ['react'], sourceType: 'script', compact: false });
  fs.writeFileSync(out, res.code);
  console.log(out, res.code.length);
}
