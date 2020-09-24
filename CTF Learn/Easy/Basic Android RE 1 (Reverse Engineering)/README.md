# Basic Android RE 1 (10 Points)
A simple APK, reverse engineer the logic, recreate the flag, and submit!
# Solved
Saya menggunakan http://www.javadecompilers.com/apk untuk mendapatkan source
```java
package com.example.secondapp;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import org.apache.commons.codec.digest.DigestUtils;

public class MainActivity extends AppCompatActivity {
    /* access modifiers changed from: protected */
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) R.layout.activity_main);
    }

    public void submitPassword(View view) {
        EditText editText = (EditText) findViewById(R.id.editText2);
        if (DigestUtils.md5Hex(editText.getText().toString()).equalsIgnoreCase("b74dec4f39d35b6a2e6c48e637c8aedb")) {
            TextView textView = (TextView) findViewById(R.id.textView);
            StringBuilder sb = new StringBuilder();
            sb.append("Success! CTFlearn{");
            sb.append(editText.getText().toString());
            sb.append("_is_not_secure!}");
            textView.setText(sb.toString());
        }
    }
}

```
Lihat pada source nya, kita di berikan beberapa petunjuk yaitu
```
CTFlearn{b74dec4f39d35b6a2e6c48e637c8aedb_is_not_secure!}
```
Tidak mungkin kita disuruh untuk menginput flag dengan md5 hash, maka dari itu saya mengdecode menggunakan https://www.md5online.org/md5-decrypt.html
```
Found : Spring2019
(hash = b74dec4f39d35b6a2e6c48e637c8aedb)
```
Flag : <b>CTFlearn{Spring2019_is_not_secure!}</b>
