title: CSS代码小抄
date: 2024-08-15
category: 代码小抄
tag: css

[TOC]

###  `CSS` 计算 `div` 的宽度和高度

```
# calc + vw 计算宽度
width: 800px; /* fallback for b*/
width: -moz-calc(100vw - (2 * 10)px);
width: -webkit-calc(100vw -(2 * 10)px);
width: calc(100vw - (2 * 10)px);

# calc + vh 计算高度
height: 800px;
height: -moz-calc(100vh - (2 * 10)px);
height: -webkit-calc(100vh - (2 * 10)px);
height: calc(100vh - (2 * 10)px);
```

<hr />
###  好看的 `hr`

```
hr {
    border: 0;
    padding: 3px;
    background: linear-gradient(135deg, red, orange,green, blue, purple);
    --mask-image: repeating-linear-gradient(135deg, #000 0px, #000 1px, transparent 1px, transparent 6px);
    -webkit-mask-image: var(--mask-image);
    mask-image: var(--mask-image);
}
```