关于“可异步调用对象”，在epub书籍里看到有关说明，如下：
- for关键字处理**可迭代对象**， await关键字处理**可异步调用对象**。
 - 作为asyncio库的终端用户，日常可见到以下两种可异步调用对象。
	 - **原生协程对象**，通过调用**原生协程函数**得到；
	 - `asyncio.Task`，通常由把协程对象传给`asyncio.create_task()`得到。
 - 然而，终端用户编写的代码不一定要使用`await`处理Task，还可以使用`asyncio.create_task(one_coro())`调用`one_coro`并发执行，不等待它返回。在spinner_async.py中的spinner协程内就是这样做的。若不打算取消或等待任务，则无须保存`create_task`返回的Task对象，仅仅创建任务就能调度协程运行。
 - 相比之下，使用`await other_coro()`立即运行`other_coro`，等待协程运行完毕，因为继续向下执行之前需要协程返回的结果。在spinner_async.py中，supervisor协程使用`res = await slow()`执行slow并获得结果。
 - 实现异步库，或者为`asyncio`库做贡献时，可能还要处理以下底层的可异步调用对象：
	 - 提供`__await__`方法、返回一个迭代器的对象；如：`asyncio.Future`实例(`asyncio.Task`是`asyncio.Future`的子类)；
	 - 以其它语言编写的对象，使用Python/C API，提供`tp_as_async.am_await`函数(类似于`__await__`方法)，返回一个迭代器。
 - 现存基准代码或许还有一种可异步调用对象——**基于生成器的协程对象**——正在走弃用流程。
 - Tips:
	 - PEP492指出，await表达式"使用`yield from`实现，外加验证参数步骤"，而且“await只接受一个可异步调用对象”；PEP492没有说明实现细节，不过引用了引入yield from的PEP380。
     ###
     当然，这书籍<Fluent Python 2nd>估计可能最多针对py3.10, 但目前使用的版本选的为3.12.x, 那么里面提到的什么走弃用流程是否出现？若有，弃用了什么？什么保留？你分析下？

---

## 分析："基于生成器的协程"在 Python 3.12 的弃用状态

《Fluent Python 2nd》最多覆盖到 Python 3.10 左右，书中说"基于生成器的协程对象正在走弃用流程"。到了 3.12，这个流程已经基本走完了。

### 已移除的

| 内容 | 移除版本 | 说明 |
|---|---|---|
| `@asyncio.coroutine` 装饰器 | 3.11 | 3.8 开始弃用，3.11 正式删除。这是把普通生成器函数"祝福"为协程的唯一官方方式。 |
| `asyncio.iscoroutine()` 对生成器返回 `True` | 3.12 | 3.12 起，传入生成器对象直接返回 `False`，asyncio 不再承认生成器是协程。 |
| `asyncio.create_task()` 接受生成器 | 3.12 | 传入生成器对象会抛出 `TypeError`，不再自动包装。 |

### 保留不变的

| 内容 | 状态 |
|---|---|
| `async def` 原生协程函数/对象 | 正常使用，唯一推荐方式 |
| `asyncio.Task` | 正常使用 |
| `asyncio.Future` 及其 `__await__` 方法 | 正常使用 |
| 提供 `__await__` 的自定义可等待对象 | 正常使用 |
| C 扩展的 `tp_as_async.am_await` | 正常使用 |
| `types.coroutine()` | 3.12 仍存在，但属于底层基础设施，非终端用户 API |

### 书中五类"可异步调用对象"在 3.12 中的对照

1. **原生协程对象**（`async def`）—— 完全正常，日常唯一该用的方式。
2. **`asyncio.Task`** —— 完全正常。
3. **提供 `__await__` 的对象**（如 `asyncio.Future`）—— 完全正常，属于库开发者领域。
4. **C 扩展提供 `tp_as_async.am_await` 的对象** —— 完全正常。
5. **基于生成器的协程对象** —— 已被 asyncio 彻底抛弃。`@asyncio.coroutine` 在 3.11 删除，3.12 中 asyncio 全面拒绝接受生成器对象作为协程。

### 结论

用 3.12 的话，只管用 `async def` 定义协程就行，基于生成器的老写法已经彻底不能用了。