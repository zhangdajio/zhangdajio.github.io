// copy_images.js
const fs = require('fs-extra');
const path = require('path');
 
hexo.extend.filter.register('after_generate', function(data) {
  const imgDir = 'public/posts/img';
  const sourceDir = 'public/img';
 
  // 确保目标目录存在
  if (!fs.existsSync(imgDir)) {
    fs.mkdirpSync(imgDir);
  }
 
  // 复制文件
  fs.copySync(sourceDir, imgDir);
});