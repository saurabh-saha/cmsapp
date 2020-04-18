import tabula

if __name__ == '__main__':
    pdffile = 'BalSheet.pdf'

    # use stream as row borders are invisible
    df = tabula.read_pdf(pdffile, pages='all', area=[110, 10, 500, 650],
                         stream=True, guess=False)
    df = df[0]
    # drop empty column
    df = df.dropna(axis=1, how='all')

    # middle column is combined - splitting here
    faultyColumn = df.columns[2]
    yColumn, pColumn = faultyColumn.split(' ')
    df[[yColumn + '.1', pColumn + '.1']] = df[faultyColumn].str.split(n=1, expand=True)
    del df[faultyColumn]

    # maintain original order
    cols = df.columns
    cols = [cols[0], cols[1], cols[-2], cols[-1], cols[2], cols[3], cols[4]]
    df = df[cols]

    # replace filename type
    df.to_csv(pdffile.replace('.pdf', '.csv'))