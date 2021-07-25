# aditiplot
Applies an Aditi filter to your plots for an improved clarity in your incredibly confusing multidimensional datasets.


## Example gallery


### A) Penguins dataset

```python
penguins = sns.load_dataset('penguins')
```


#### An inferior `seaborn` visualization

```python
g = sns.relplot(x='bill_length_mm',
                y='bill_depth_mm',
                hue='species',
                col='sex',
                data=penguins)
```

![png](./gallery/output_6_0.png)
    

#### The superior `aditiplot`

```python
aditi.plot(penguins)
```

![png](./gallery/output_8_1.png)
    

### B) Tips dataset

```python
tips = sns.load_dataset('tips')
```


#### An inferior `seaborn` visualization

```python
sns.relplot(
    data=tips, x="total_bill", y="tip", col="time",
    hue="time", size="size", style="sex",
    palette=["b", "r"], sizes=(10, 100)
);
```

![png](./gallery/output_12_0.png)
    

#### The superior `aditiplot`

```python
aditi.plot(tips, hue='size');
```

![png](./gallery/output_14_0.png)


### C) FMRI dataset

```python
fmri = sns.load_dataset('fmri')
```

#### An inferior `seaborn` visualization

```python
sns.relplot(
    data=fmri, x="timepoint", y="signal", col="region",
    hue="event", style="event", kind="line",
);
```
    
![png](./gallery/output_18_0.png)

#### The superior `aditiplot`

```python
aditi.plot(fmri, kind='line');
```

![png](./gallery/output_20_0.png)
