---
bibliography:
- 'deep.bib'
---

=1

[UTF8]{}[gbsn]{}

介绍神经网络中的深度学习 {#intro}
========================

学习系统的哪些可修改的组件负责其成功或失败？
这些组件如何改变能够提升性能？ 这被称为 [*fundamental credit assignment
problem*]{} [@Minsky:63]. 有通用的credit assignment
methods来处理[*universal problem
solvers*]{}，这些方法在各种理论意义上是时间最优的

(Sec. \[unirl\])。
本篇综述相反将关注更窄但是有重大商业应用的[*人工神经网络*]{}
(NNs)中的一个子领域[*深度学习*]{} (DL) 。

一个标准的神经网络由许多简单被称为神经元的连接处理器组合，每一个生成一个真是值激活的序列。
输入神经元通过感知环境的传感器被激活，其他神经元通过连接先前激活神经元的权重被激活
(细节见 Sec. \[notation\]). 有一些神经元也许会通过触发动作影响环境。
[*学习*]{} or [*credit
assignment*]{}是关于发现权重来使得NN具备[*期望的*]{} 行为,
比如自动驾驶。
按照问题不同以及神经元如何连接，这种行为也许要求长期的随意计算情况
(Sec. \[caps\]), 在那里每一种情况都会转换
(经常是以非线性的方式)网络的激活。 深度学习是关于精确地在 [*多种*]{}
情况下赋值credit。

考虑了[*许多*]{}这种情况的[*浅层*]{} NN-like模型已经研究了许多年了
(Sec. \[1940\])。 具有几种前向非线性层的神经元早在1960年(Sec. \[1965\])
和1970(Sec. \[1970\])年就已经提出了。 一种高效地基于训练的[*监督学习*]{}
(SL)梯度下降方法, 被称为 [*反向传播*]{}
(BP)的随机深度的不同网络在1960年和1970年就被提出, 并且在1981年应用到了NN
(Sec. \[1970\])。 然而，基于BP训练具有[*多成网络层*]{} 的[*深度*]{} NNs,
已经在1980年就被发现在实际过程中难以应用(Sec. \[1990\]),
早在1990年这个问题就已经是研究热点(Sec. \[1991a\])。
DL通过[*非监督学习*]{} (UL), 例如, Sec. \[1991b\] (1991), Sec. \[2006\]
(2006)在某一程度上变得切实可行。
1990年和2000年在纯监督DL中(Sec. \[super\])见证了许多性能的提升。
在接下来的几年中，深度学习终于吸引了广泛的关注，在许多不同的重要应用中都超过了可选的机器学习方法，比如基于kernel的方法[@Vapnik:95; @advkernel]。
事实上，2009年以来，监督深度NNs已经在许多官方国际模式识别竞赛中获得了巨大的成功
(比如, Sec. \[2009\], \[2011\], \[2012\], \[2013\]),
实现了第一个在有限的领域超越人类视觉模式识别结果 (Sec. \[2011\], 2011)。
深度NNs也已经在许多通用的[*增强学习*]{}
(RL)领域中获得了广泛的应用(Sec. \[deeprl\])。

[*前向*]{} (非周期性) NNs (FNNs) 和 [*循环*]{} (周期性) NNs
(RNNs)也赢得了许多比赛 (Sec. \[1994\], \[2003\], \[2009\], \[2011\],
\[2012\], \[2013\]).
某种程度上，RNNs是所有网络中最深的网络(Sec. \[caps\])—它们是通用的计算机

但是比FNNs更加强大，并原则上可以创建和处理任意输入模式序列的记忆[例如.,
@siegelmann91turing; @schmidhuber1990].
不像传统的自动顺序程序合成方法 [例如.,
@waldinger69; @balzer1985; @soloway1986; @Deville:94],
RNN以自然而有效的方式混合顺序和并行信息处理学习程序, exploiting the
massive parallelism viewed as crucial for sustaining the rapid decline
of computation cost observed over the past 75 years.

The rest of this paper is structured as follows. Sec. \[notation\]
introduces a compact, event-oriented notation that is simple yet general
enough to accommodate both FNNs and RNNs. Sec. \[caps\] introduces the
concept of [*Credit Assignment Paths*]{} (CAPs) to measure whether
learning in a given NN application is of the [*deep*]{} or [*shallow*]{}
type. Sec. \[themes\] lists recurring themes of DL in SL, UL, and RL.
Sec. \[super\] focuses on SL and UL, and on how UL can facilitate SL,
although pure SL has become dominant in recent competitions
(Sec. \[2009\]–\[dominant\]). Sec. \[super\] is arranged in a historical
timeline format with subsections on important inspirations and technical
contributions. Sec. \[deeprl\] on deep RL discusses traditional
[*Dynamic Programming*]{} (DP)-based RL combined with gradient-based
search techniques for SL or UL in deep NNs, as well as general methods
for direct and indirect search in the weight space of deep FNNs and
RNNs, including successful policy gradient and evolutionary methods.
