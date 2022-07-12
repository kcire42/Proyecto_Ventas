from msilib import datasizemask
from pylogix import PLC
import time


    # ret = comm.Read("Start_PB")
    # print(ret.TagName, ret.Value, ret.Status)
    
def read_data():
    with PLC("10.99.182.13") as comm:
        data = []
        # save_data = comm.Read('save_data')
        # print(save_data.TagName,save_data.Value,save_data.Status)
        part_number = comm.Read('DB26.Setup.Part_Number')
        #como hacer el casting de byte code a str
        part_number_str = ''.join(c for c in part_number.Value.decode('utf-8','ignore') if c.isprintable())
        #print(part_number_str)
        pattern_sewing = comm.Read('DB26.Setup.Pattern_Sewing')
        seccion_1_Stitch_number = comm.Read('DB26_Sew.Setup.Seccion_1.Stitch_Number')
        seccion_1_Lim_inf = comm.Read('DB26_Sew.Setup.Seccion_1.Tension_Lim_Inf')
        seccion_2_Stitch_number = comm.Read('DB26_Sew.Setup.Seccion_2.Stitch_Number')
        seccion_2_Lim_inf = comm.Read('DB26_Sew.Setup.Seccion_2.Tension_Lim_Inf')
        seccion_3_Stitch_number = comm.Read('DB26_Sew.Setup.Seccion_3.Stitch_Number')
        seccion_3_Lim_inf = comm.Read('DB26_Sew.Setup.Seccion_3.Tension_Lim_Inf')
        seccion_4_Stitch_number = comm.Read('DB26_Sew.Setup.Seccion_4.Stitch_Number')
        seccion_4_Lim_inf = comm.Read('DB26_Sew.Setup.Seccion_4.Tension_Lim_Inf')
        qty_of_stitches = comm.Read('Qty_of_Stitches')
        tension = comm.Read('Tension_Data[0]',200)
        #obtener tipo de dato de mis variables
        #print(part_number.TagName,type(part_number_str))
        # print(pattern_sewing.TagName,type(pattern_sewing.Value))
        # print(seccion_1_Stitch_number.TagName,type(seccion_1_Stitch_number.Value))
        # print(seccion_1_Lim_inf.TagName,type(seccion_1_Lim_inf.Value))
        # print(qty_of_stitches.TagName,type(qty_of_stitches.Value))
        data.append({part_number.TagName : part_number_str })
        data.append({pattern_sewing.TagName:pattern_sewing.Value})
        data.append({seccion_1_Stitch_number.TagName : seccion_1_Stitch_number.Value})
        data.append({seccion_1_Lim_inf.TagName :seccion_1_Lim_inf.Value})
        data.append({seccion_2_Stitch_number.TagName : seccion_2_Stitch_number.Value})
        data.append({seccion_2_Lim_inf.TagName :seccion_2_Lim_inf.Value})
        data.append({seccion_3_Stitch_number.TagName : seccion_3_Stitch_number.Value})
        data.append({seccion_3_Lim_inf.TagName :seccion_3_Lim_inf.Value})
        data.append({seccion_4_Stitch_number.TagName : seccion_4_Stitch_number.Value})
        data.append({seccion_4_Lim_inf.TagName :seccion_4_Lim_inf.Value})
        data.append({qty_of_stitches.TagName:qty_of_stitches.Value})
        data.append(tension.Value)
        #print(data)
        return(data)
        

def write_data(data):
    
    file_1 = open("SB06_Datos_costura.txt",'a')
    file_1.write(str(data))
    file_1.write("\n")
    file_1.close() 


def main():
    with PLC("10.99.182.13") as comm:
        while True:
            save_data = comm.Read('save_data')
            #print(save_data.TagName,save_data.Value,save_data.Status)
            #save_data.Value.watch()
            #print("Esperando un respuesta")
            if save_data.Value == True:
                data = read_data()
                print(data)
                write_data(data)
                if save_data.Value==False:
                    #print(save_data.TagName,save_data.Value,save_data.Status)
                    main()

if __name__ =='__main__':
    main()
    
            
            



