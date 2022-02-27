#!/bin/bash
# 确保进程有足够的数量
# macos下，date命令功能少，不可用。可用brew安装gdate替换使用
# author:lin
source ~/.bashrc
# 确保进程数在一定的数量下
object_process_num=5  # 目标进程数
root_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)""/" #当前shell脚本的路径(最后带有/)
if [[ $# -lt 1 ]]
then
  echo "请输入文件名（不需要输入路径）"
fi
python_file_name=$1
python_path=${root_path}${python_file_name}
log_path=$root_path'logs/'


while true; do
  python_process_list=$(ps -ef | grep "$python_path" | grep -v 'grep' | wc -l)
  echo "当前进程数：$python_process_list"
  while [ "$python_process_list" -lt $object_process_num ]; do
    echo "当前进程数：$python_process_list"
    now_time=$(date +'%Y-%m-%d-%H-%M-%S')
    echo "当前时间${now_time}"
    # 启动进程
    tag=$(date +'%Y_%m_%d_%H_%M_%S')$((RANDOM%100))
    nohup python3 -u "${python_path}" "${tag}" >> "${log_path}${python_file_name}._${tag}".log 2>&1 &
    echo "${now_time}启动了一个进程"
    sleep 1
    python_process_list=$(ps -ef | grep "$python_path" | grep -v 'grep' | wc -l)
  done
  sleep 1s

done
