import seaborn as sns


def deorganize(data, x=None, y=None, hue=None, size=None, style=None, **kwargs):
    """Make some chaos

    The idea is that we want to use as many plotting dimensions
    (e.g. marker color, marker shape, etc.) as possible when
    we plot our data. So given a multidimensional dataset, this
    function assigns fields (column names of the dataset) to
    these plotting parameters. The plotting dimensions `row`
    and `col` can only aid in organizing the plot, which
    would defeat the purpose, so we decline to assign fields 
    to these plotting dimensions, choosing instead to cram as
    many dimensions as possible into a single matplotlib axis.

    Parameters
    ----------
    data : `pd.DataFrame`
        Input dataset
    x, y : str, str
        Names of variables in `data`
    hue : str
        Column name in `data` that will group data by color
    size : str
        Column name in `data` that will group data by marker size
    style : str
        Column name in `data` that will group data by marker style
    kwargs : dict
        Other keyword arguments that are passed through to some underlying
        plotting function
    
    Returns
    -------
    data : `pd.DataFrame`
        (Unchanged) dataset
    kwargs : dict
        Dictionary of plotting parameters to pass through to some underlying
        plotting function
    """

    # Extract kwargs
    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)
    hue = kwargs.pop('hue', None)
    size = kwargs.pop('size', None)
    style = kwargs.pop('style', None)

    # Get data types of input dataset
    dtypes = data.dtypes
    # Remove used dimensions from dtypes
    dtypes = dtypes.drop([x, y, hue, size, style], errors='ignore')

    # Split dtypes into ordinal (object) and numerical (int or float)
    fields_O = dtypes[dtypes.values == 'O'].index
    fields_N = dtypes[dtypes.values != 'O'].index

    # (Re)Assign parameters
    # ---------------------
    # Assign x if not provided
    if x is None:
        # Choose first field in the dataset with a numerical dtype
        # (if possible)
        if len(fields_N):
            x = fields_N[0]
            # Remove field (now that it has been assigned)
            fields_N = fields_N.drop(x)
            dtypes = dtypes.drop(x)
        # Otherwise, just choose the first field in the dataset
        # irrespective of dtype
        else:
            x = dtypes.index[0]
            # Remove field (now that it has been assigned)
            fields_O = fields_O.drop(x)
            dtypes = dtypes.drop(x)
    # Same thing for `y`
    if y is None:
        if len(fields_N):
            y = fields_N[0]
            fields_N = fields_N.drop(y)
            dtypes = dtypes.drop(y)
        else:
            y = dtypes.index[0]
            fields_O = fields_O.drop(y)
            dtypes = dtypes.drop(y)
    # Assign `hue` to the first available ordinal field
    if hue is None:
        if len(fields_O):
            hue = fields_O[0]
            fields_O = fields_O.drop(hue)
            dtypes = dtypes.drop(hue)
        # Settle for a numerical field if no ordinal fields available
        else:
            hue = fields_N[0]
            fields_N = fields_N.drop(hue)
            dtypes = dtypes.drop(hue)
    # Same thing for size
    if size is None:
        if len(fields_O):
            size = fields_O[0]
            fields_O = fields_O.drop(size)
            dtypes = dtypes.drop(size)
        else:
            size = fields_N[0]
            fields_N = fields_N.drop(size)
            dtypes = dtypes.drop(size)
    # Same thing for style
    if style is None:
        if len(fields_O):
            style = fields_O[0]
            fields_O = fields_O.drop(style)
            dtypes = dtypes.drop(style)
        else:
            style = fields_N[0]
            fields_N = fields_N.drop(style)
            dtypes = dtypes.drop(style)

    # Redefine kwargs
    kwargs['x'] = x
    kwargs['y'] = y
    kwargs['hue'] = hue
    kwargs['size'] = size
    kwargs['style'] = style

    return data, kwargs


def plot(data, **kwargs):
    """Make an Aditi plot!"""

    # Deorganize
    data, kwargs = deorganize(data, **kwargs)

    # Make call to seaborn relplot
    g = sns.relplot(data=data, legend=False, **kwargs)

    # Axis formatting
    g.set(xticklabels=[])
    g.set(xlabel=None)
    g.set(ylabel=None)
