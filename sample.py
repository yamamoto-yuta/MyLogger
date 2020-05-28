import os
import logging

# モジュールをインポート
from my_logger import get_logger

if __name__ == '__main__':
    
    print('start')
    
    # ログフォルダ・ログファイル設定
    log_dir = './'
    log_txt = os.path.join(log_dir, 'log_sample.txt')
    
    # ロガー作成
    lg = get_logger(__name__, log_txt)
    
    lg.debug('ロギング 開始')

    try:
        # --ここに処理を書く--
        
        # ↓試しに例外を発生させてみる
        raise ValueError('テスト バリューエラー')
    except:
        lg.exception('例外を記録 ここから↓')
        lg.debug('ここまで↑')

    lg.debug('ロギング 終わり')
    
    print('end')
    
    # `log_sample.txt` というファイルが生成される