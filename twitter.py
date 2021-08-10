import tweepy
from tkinter import messagebox

def tweet(text, filename1, filename2):
    # 取得した各種キーを代入する
    CK = "0HoE9YTmKFBRibsKCpFEMsLo9"
    CS = "fdzkfi59XBM1NI6UrsOedzXmgR3l3uQrmalkzDKXxPBVWvIVs5"
    AT = "900534491638136833-X4MG8kwyf0GWwf6o3TgxqfgO7yctDA3"
    AS = "8gGm31vA2YE3WT6VqZZ3BR9ag5YzHcbf1I7lmfTLFura2"

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    media_ids = []

    if filename2:
        file_names = [filename1, filename2]
        for filename in file_names:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)
            api.update_status(status=text, media_ids=media_ids)

    elif filename1:
        file_names = [filename1]
        api.update_with_media(status=text, filename=filename1)

    else:
        file_names = []
        api.update_status(text)