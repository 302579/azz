#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

# CSS和JS文件名映射
css_mapping = {
    'css/main-主样式.css': 'css/main.css',
    'css/map-地图样式.css': 'css/map.css',
    'css/game-游戏样式.css': 'css/game.css',
    'css/knowledge-知识拓展样式.css': 'css/knowledge.css',
    'css/nav-导航样式.css': 'css/nav.css'
}

js_mapping = {
    'js/map-地图脚本.js': 'js/map.js',
    'js/game-游戏脚本.js': 'js/game.js',
    'js/knowledge-知识拓展脚本.js': 'js/knowledge.js'
}

print("=" * 60)
print("更新HTML文件中的CSS和JS引用")
print("=" * 60)

# 获取所有HTML文件
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 替换CSS引用
    for old_name, new_name in css_mapping.items():
        content = content.replace(old_name, new_name)
    
    # 替换JS引用
    for old_name, new_name in js_mapping.items():
        content = content.replace(old_name, new_name)
    
    # 如果内容有变化，写回文件
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 更新文件: {html_file}")
    else:
        print(f"⏭️  无需更新: {html_file}")

print("\n" + "=" * 60)
print("验证更新结果")
print("=" * 60)

# 验证：检查是否还有中文文件名引用
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否还有带中文的CSS/JS引用
    if re.search(r'(css|js)/[^"\']*[\u4e00-\u9fff]', content):
        print(f"⚠️  {html_file} 中仍有中文文件名引用")
    else:
        print(f"✅ {html_file} 引用已全部更新为英文")

print("\n✅ CSS和JS文件引用更新完成！")
