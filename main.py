def calculate_max_draw_down(df):
    '''
    Método auxiliar para el cálculo de Max Draw Down
    MainDrawDown = (main_min / main_max) - 1
    PrevDrawDown = (prev_min / prev_max) - 1
    Max Draw Down = Higher value between MainDrawDown and PrevDrawDown
    '''

    res_tuple = None

    classinfinity_code = df.loc[df['return'].idxmax()]['classinfinity_code']
    cod_fundinfinity = df.loc[df['return'].idxmax()]['cod_fundinfinity']
    main_max = df.loc[df['return'].idxmax()]['return']

    dat_fact_main_max = df.loc[df['return'].idxmax()]['dat_fact']

    df_main_min = df[(df['dat_fact'] >= dat_fact_main_max)]

    main_min = df_main_min.loc[df_main_min['return'].idxmin()]['return']

    df_prev_min = df[(df['dat_fact'] <= dat_fact_main_max)]

    prev_min = None
    if not df_prev_min.empty:
        prev_min = df_prev_min.loc[df_prev_min['return'].idxmin()]['return']

        dat_fact_prev_min = df_prev_min.loc[df_prev_min['return'].idxmin()]['dat_fact']

        df_prev_max = df[(df['dat_fact'] <= dat_fact_prev_min)]

        prev_max = None
        if not df_prev_max.empty:
            prev_max = df_prev_max.loc[df_prev_max['return'].idxmax()]['return']

    max_draw_down = 0
    if main_max and main_min:
        if prev_min and prev_max:
            if main_max != 0 and prev_max != 0:
                main_draw_down = (main_min / main_max) - 1
                prev_draw_down = (prev_min / prev_max) - 1

                max_draw_down = main_draw_down if main_draw_down < prev_draw_down else prev_draw_down

        else:
            if main_max != 0:
                main_draw_down = (main_min / main_max) - 1

    if classinfinity_code and cod_fundinfinity:
        res_tuple = (classinfinity_code,cod_fundinfinity,max_draw_down)

    return res_tuple
