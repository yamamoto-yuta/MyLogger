import os
import logging

def get_logger(logger_name, log_file, s_fmt='%(message)s', f_fmt='%(message)s'):
    """
    ロガーを取得する関数
    
    Parameters
    ----------
    logger_name : str
        ロガーの名前
    logger_file : str
        ログファイルの出力先
    
    Returns
    -------
    logger : ?
        ロガー
    
    See Also
    --------
    Pythonでログを出力するコード例【logging】
    https://srbrnote.work/archives/1656
    
    """
    
    # ロガー作成
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # ストリームハンドラ作成
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(s_fmt))

    # ロガーに追加
    logger.addHandler(stream_handler)

    # ファイルハンドラ作成
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(f_fmt))

    # ロガーに追加
    logger.addHandler(file_handler)

    return logger

