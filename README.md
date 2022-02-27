# 图片清洗,识别过滤
通过百度识图将不是建筑的图片过滤掉
图片数量约为150万,约200g,存放于oss存储桶
10台4核2g服务器60线程约不到一天时间

## 文件
```
categorize_images.py    #运行主要程序
ensure_process_num.sh   #多线程运行shell脚本
get_token.py            #百度识图AK SK信息
method_1_api_request.py #线上api识图
method_2_sdk.py         #本地sdk识图
push_path_to_redis.py   #将需要识别的图推到redis队列

```
## KEY生成说明
1. AK SK
   - API 和 SDK 调用均需获取 AK SK 信息。 当前项目AK SK 等文件，均记录在 conf.py 文件，未上传GIT，示例如下。
   ```
   APP_ID = '你的 App ID'
   API_KEY = '你的 Api Key'
   SECRET_KEY = '你的 Secret Key'
   ```

## 项目运行步骤参考
1. 步骤一：配置相应AK SK 文件，并建立一个空的conf.py
2. 步骤二：运行调用程序, 前文提到的调用方式可任选其一，method_1_api_request 或者 method_2_sdk (一个百度机器跑，一个本地跑)
3. 步骤三：根据识别结果将建筑类与非建筑类文件移至相应文件夹，进行文件初步二分类。示例程序 categorize_images.py
4. 备注说明：根据实际情况，修改需读取img文件地址信息，对于批量文件读取，需进行循环调用


```
# 填写ridis机器信息

# 将需要识别的图片的路径修改到push_path_to_redis.py

# 推到ridis队列
python3 push_path_to_redis.py

# 多线程启动，启动的程序数量在ensure_process_num.sh里面改
nohup bash ensure_process_num.sh categorize_images.py >> ensure_process_num.sh.log 2>&1 &
```
