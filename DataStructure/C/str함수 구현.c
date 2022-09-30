<strcat>
void MyStrcat(char str[], char str2[]) {

	int w = strlen(str);
	int i = 0;
	while (str2[i] != '\0') {
		str[w++] = str2[i++];
	}
}

<strcpy>
char *strcpy( char *str2, char *str1)
{
char *p=str2;
while(*p++ = *str1++); //
return str2;
}

int main(char *copy)
{
char a[100]={"hello world"};
char b[100];

strcpy(b,a);

printf("%s\n%s\n",a,b);
}

<strcmp>
int strcmp(const char *s1, const char s2)
{
	unsigned char c1, c2;

	while (1) {
    	/* s1, s2 문자열에서 순서대로 한글자씩 가져옵니다. */
		c1 = *s1++;
		c2 = *s2++;
		/* 한글자씩 비교하고 다르면 -1 또는 1 리턴합니다. */
		if (c1 != c2)
			return c1 < c2 ? -1 : 1;
		if (!c1)
			break;
	}
    /* 루프를 빠져나오면 두 문자열이 같다는 의미이므로 0을 리턴합니다. */
	return 0;
}

<strchr>
char *strchr(const char *s, int c)
{
        /*
         * s 문자열의 처음 문자부터 c 문자와 같지 않으면
         * 루프를 계속 돕니다.
         * 같으면 루프를 종료하고 현재 s의 위치를 리턴합니다.
         */
        for (; *s != (char)c; ++s)
                if (*s == '\0')
                        return NULL;
        return (char *)s;
}

<strstr>
char *strstr(const char *s1, const char s2)
{
	size_t l1, l2;

	l2 = strlen(s2);
    
	/* s2 문자열의 길이가 0이라면 무조건 매칭으로 보고 s1의 시작주소를 반환합니다. */
	if (!s2)
		return (char *)s1;

	l1 = strlen(s1);
	/* 남은 l1의 길이가 l2 길이 보다 작다면, 비교할 의미가 없으므로 NULL을 리턴합니다. */
	while (l1 >= l2) {
		l1--;
		/*
		 * s1의 포인터 위치를 이동하면서,
		 * 현재 s1과 s2의 메모리를 s2의 사이즈만큼 비교합니다.
		 * 같으면 현재 s1의 포인터를 리턴합니다.
		 */
		if (!memcmp(s1, s2, l2))
			return (char *)s1;
		s1++;
	}
	return NULL;
}