# JKS para assinar o APK. O alias é "EchoPTBR" e todas as senhas são "EchoPTBR".

## PK8:

`EchoPTBR.keystore (EchoPTBR.jks) criado com o Android Studio.`

`keytool -importkeystore -srckeystore EchoPTBR.keystore -destkeystore intermediate.p12 -srcstoretype JKS -deststoretype PKCS12`

`openssl pkcs12 -in intermediate.p12 -nodes -out intermediate.rsa.pem`

`openssl pkcs8 -topk8 -outform DER -in intermediate.rsa.pem -inform PEM -out private.pk8 -nocrypt`

## X509Certificate:

`keytool -list -rfc -keystore EchoPTBR.keystore -alias EchoPTBR -storepass EchoPTBR`