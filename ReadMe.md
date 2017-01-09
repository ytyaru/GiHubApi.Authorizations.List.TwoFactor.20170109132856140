# このソフトウェアについて

GiHubApi.Authorizations.List.TwoFactor.20170109132856140は私個人が学習目的で作成したソフトウェアである。

GitHubのTwoFactor認証アカウントからAccessTokenを取得するPythonスクリプト。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
* [WinAuth](https://winauth.com/download/)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

* [GitHubアカウント](https://github.com/join?source=header-home)を作成する
* [AccessToken](https://github.com/settings/tokens)を1つ以上作成する
* [Two-Factor認証を有効にする設定](https://github.com/settings/two_factor_authentication/intro)を行う
* Main.pyにGitHubのusernameとpasswordを指定する
* [WinAuth](https://winauth.com/download/)などでOTP(One-Time-Password)を取得する

# 実行

```dosbatch
python Main.py
```

WinAuthなどでOTPを取得してから変更されるまでの間(30秒間)に、`Main.py`を実行する。

# 結果

[List your authorizations API](https://developer.github.com/v3/oauth_authorizations/#list-your-authorizations)の結果が`GiHubApi.Authorizations.List.{username}.json`ファイルに出力される。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
