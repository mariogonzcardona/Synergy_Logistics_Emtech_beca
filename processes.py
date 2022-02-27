import pandas as pd

def generate_df():
    df_logistics=pd.read_csv('synergy_logistics_database.csv',index_col=0)
    df_logistics['date'] = pd.to_datetime(df_logistics['date'],format='%d/%m/%y')
    return df_logistics

# 10 rutas mas demandadas para importacion y exportacion
def option_1(option):
    df_logistics=generate_df()
    df_imports=df_logistics.loc[df_logistics['direction'] == 'Imports']
    df_exports=df_logistics.loc[df_logistics['direction'] == 'Exports']
    
    if option == 1:
        # Contar con respecto a Imports y las rutas de origen y destino considerando las 10 mas demandadas
        res_imports=df_imports[['origin','destination']].value_counts()
        print("|:-------Rutas mas demandadas-------| Cant|")
        print(res_imports[0:10].to_markdown())
    elif option == 2:
        # Contar con respecto a Exports y las rutas de origen y destino considerando las 10 mas demandadas
        df_res_exports=df_exports[['origin','destination']].value_counts()
        print("|:---Rutas mas demandadas----| Cant|")
        print(df_res_exports[0:10].to_markdown())
    
# Cuáles son los 3 medios de transporte más importantes para importaciones y exportaciones
def option_2(option):
    df_logistics=generate_df()
    df_imports=df_logistics.loc[df_logistics['direction'] == 'Imports']
    df_exports=df_logistics.loc[df_logistics['direction'] == 'Exports']
    
    if option == 1:
        # Proceso para obtener el valor total por cada tipo de transporte (Rail, Sea, Air, Road) por Import
        df_trans_imp=df_imports['transport_mode'].unique()
        dict_imp_tot={}
        for t in df_trans_imp:
            df_res_tmp=df_imports.loc[df_imports['transport_mode'] == t]
            dict_imp_tot[t]=df_res_tmp['total_value'].sum()
        
        df_total_imp=pd.DataFrame.from_dict(dict_imp_tot, orient='index',columns=['total_imp'])
        df_total_imp=df_total_imp.sort_values(by=['total_imp'],ascending=False)
        print(df_total_imp['total_imp'].apply(lambda x: "${:,.2f}".format((x))).to_markdown())
        
    elif option == 2:
        # Proceso para obtener el valor total por cada tipo de transporte (Rail, Sea, Air, Road) por Export
        df_trans_exp=df_exports['transport_mode'].unique()
        dict_exp_tot={}
        for t in df_trans_exp:
            df_res_tmp=df_exports.loc[df_exports['transport_mode'] == t]
            dict_exp_tot[t]=df_res_tmp['total_value'].sum()

        df_total_exp=pd.DataFrame.from_dict(dict_exp_tot, orient='index',columns=['total_exp'])
        df_total_exp=df_total_exp.sort_values(by=['total_exp'],ascending=False)
        print(df_total_exp['total_exp'].apply(lambda x: "${:,.2f}".format((x))).to_markdown())
        
# Cuáles son los países que generan el 80% del valor de importaciones y exportaciones
def option_3(option):
    df_logistics=generate_df()
    df_imports=df_logistics.loc[df_logistics['direction'] == 'Imports']
    df_exports=df_logistics.loc[df_logistics['direction'] == 'Exports']
    
    if option ==1:
        # Total de importaciones
        total_source_value=df_imports['total_value'].sum()

        # Para obtener el total de importaciones en formato monetario
        total_print='${:,.2f}'.format(total_source_value)
        print(f'El Total de importaciones es de: {total_print}')
        
        # Generar lista de origenes para Imports
        source_list=df_imports['origin'].unique()
        
        # Generar listado para cada origen sumando el total_value por cada origen
        source_total=[]
        for origin in source_list:
            source=df_imports.loc[df_imports['origin']==origin]
            source_total.append([origin,source['total_value'].sum()])
            
        # Creamos un dataframe para el total de Países con respecto a Imports
        # Agregamos columnas de ['percent', 'cum_percent'], para tabla de frecuencia acumulada
        df_sources = pd.DataFrame(source_total, columns = ['Origin', 'total_value'])
        df_sources=df_sources.sort_values(by=['total_value'],ascending=False)
        df_sources['percent']=(df_sources['total_value'] / total_source_value)
        df_sources['cum_percent']=df_sources['percent'].cumsum()
        print(df_sources[:8].to_markdown())
        
    elif option == 2:
        # Total de exportaciones
        total_target_value=df_exports['total_value'].sum()

        # Para obtener el total de exportaciones 
        total_print='${:,.2f}'.format(total_target_value)
        print(f'El Total de exportaciones es de: {total_print}')
        
        # Generar lista de destino para exports
        target_list=df_exports['destination'].unique()
        
        # Generar listado para cada destino sumando el total_value por cada destino
        target_total=[]
        for dest in target_list:
            destin=df_exports.loc[df_exports['destination']==dest]
            target_total.append([dest,destin['total_value'].sum()])
            
        # Creamos un dataframe para el total de Países con respecto a Exports
        # Agregamos columnas de ['percent', 'cum_percent'], para tabla de frecuencia acumulada
        df_target = pd.DataFrame(target_total, columns = ['destination', 'total_value'])
        df_target=df_target.sort_values(by=['total_value'],ascending=False)
        df_target['percent']=(df_target['total_value'] / total_target_value)
        df_target['cum_percent']=df_target['percent'].cumsum()
        print(df_target[:13].to_markdown())
