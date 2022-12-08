import module.SayHello as App

def  run():
    app = App.SayHello("Git")
    #app.say()
    app = App.SayHello("Git Hub")
    app.say()

if __name__ == '__main__':
    run()
