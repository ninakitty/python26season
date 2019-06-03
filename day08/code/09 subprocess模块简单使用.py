import subprocess

cmd = input('请输入指令:')
conn = subprocess.Popen(
    cmd,
    shell=True,
    stdout=subprocess.PIPE, #标准正确输出
    stderr=subprocess.PIPE, #标准错误输出
)

print('正确输出',conn.stdout.read().decode('gbk'))
print('错误输出',conn.stderr.read().decode('gbk'))



