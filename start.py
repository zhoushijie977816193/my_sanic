# /user/bin/env python3.6
# -*- coding: utf-8 -*-
# author zhoushijie 2019.11.22


from manage import app
from routes import book


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8030", debug=True)
