# MultiUserLogin
Multi-user login system using Django using proxy models and groups permissions to limit access to certain views depending on the user's type.

# Example users :
## Utilisateurs :
Can only view '*homepage/*' and '*cours/*'. 
```
username = jesuisetudiant1
password = iamstudent1
```
```
username = jesuisetudiant2
password = iamstudent2
```
## Educateurs :
Can view '*homepage/*' and '*rapports/*' and add '*cours/*'. 
```
username = jesuiseducateur1
password = iamteacher1
```
## Psychologues :
Can view '*homepage/*' and '*cours/*' and add '*rapports/*'. 
```
username = jesuispsychologue1
password = iampsychologue1
```
## ADMIN :
```
username = admin
password = admin
```

