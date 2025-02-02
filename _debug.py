# 示例检查代码是否有语法错误
try:
    # 这里假设你在本地环境有Python解释器
    import api.random

    print("语法检查通过")
except SyntaxError as e:
    print(f"语法错误: {e}")
