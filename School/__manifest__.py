{
    'name': 'School',
    'summary':"""Test Management Software""",
    'description':"""
        Test Model
    """,
    'author':"HuuBien",
    'website':"http://www.mycompany.com",
    'category': 'toolll',
    'version':'16.0.1.0.0',
    
    'depends':['base'],   
    'data':
        [
            # # "views/estate_property_views.xml",
            # # "views/estate_menu.xml",
            "security/security.xml",
            "security/ir.model.access.csv",
            "views/student_view.xml",
            "views/teacher_view.xml",
            "views/subject_view.xml"
            
        ],
    'demo':[],
    # 'images': [
    #     "static/voi.jpg",
    # ],
    'installable':True,
    'application':True,
    'auto_install':False   
}