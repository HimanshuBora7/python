#Consider a company that creates 3D printed models of designs that 
#users submit. Designs that need to be printed are stored in a list, and after 
#being printed they’re moved to a separate list

def print_models(completed_design,uncompleted_design):
 """Simulate printing each design, until none are left. Move each design to completed_models after printing."""

 while uncompleted_design:
      current_design = uncompleted_design.pop()
      print(f"current design : {current_design}")
      completed_design.append(current_design)

def show_completed(completed_design):
        print("the following models has been printed ")
        for design in completed_design:
            print(design)

uncompleted_design=['rocket','engine','shafts','metal arm']
completed_design=[]

print_models(completed_design,uncompleted_design)
show_completed(completed_design)
