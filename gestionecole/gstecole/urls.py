"""
URL configuration for gstecole project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_ecole.views import home,sections,Options,Classes,Inscriptions,Eleves,Paiements,frais,ajoutersection,ajouteroption,ajouterclasse,ajouterinscription,ajoutereleve,ajouterpaiement,ajouterfrais,addSections,addOptions,addClasse,addEleve,addInscription,addPaiements,addFrais,deleteSection,deleteOption,deleteInscription,deletePaiement,deleteClasse,deleteEleve,deleteFrais,modifierSection,updateSection, modifierSection,modifierOption,updateOption,updateClasse,modifierClasse,modifierInscription,updateInscription,modifierEleve,updateEleve,modifierPaiement,updatePaiement,modifierFrais,updateFrais,SectionDetails,Sectioninfo
from app_ecole.views import logins,sign_in,user,forme,sign_up,log_out,rapportsec,rapportopt,rapportcla,rapportins,rapportele,rapportpai,rapportfra,deleteUser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name = "home"),
    path('sign_in', sign_in, name="sign_in"),
    path('', logins, name="login"),
    path('user/', user, name="user"),
    path('sections/', sections, name= "sections" ),
    path('sign_up/', sign_up, name="sign_up"),
    path('forme/', forme, name="forme"),
    path('Options/', Options, name= "Options" ),
    path('classes/', Classes, name= "Classes" ),
    path('inscriptions/', Inscriptions, name= "Inscriptions" ),
    path('Eleves/', Eleves, name= "Eleves" ),
    path('Paiements/', Paiements, name= "Paiements" ),
    path('frais/', frais, name= "frais" ),
    path('ajoutersection/', ajoutersection, name= "ajoutersection" ),
    path('ajouteroption/', ajouteroption, name= "ajouteroption" ),
    path('ajouterclasse/', ajouterclasse, name= "ajouterclasse" ),
    path('ajouterinscription/', ajouterinscription, name= "ajouterinscription" ),
    path('ajoutereleve/', ajoutereleve, name= "ajoutereleve" ),
    path('ajouterpaiement/', ajouterpaiement, name= "ajouterpaiement" ),
    path('ajouterfrais/', ajouterfrais, name= "ajouterfrais" ),
    path('addSections /', addSections, name="addSections" ),
    path('addOptions /', addOptions, name="addOptions" ),
    path('addClasse /', addClasse, name="addClasse" ),
    path('addEleve /', addEleve, name="addEleve" ),
    path('addInscription /', addInscription, name="addInscription" ),
    path('addPaiments /', addPaiements, name="addPaiements" ),
    path('addFrais /', addFrais, name="addFrais" ),
    path('deleteSection<str:id>/', deleteSection, name="deleteSection" ),
    path('deleteOption<str:id>/', deleteOption, name="deleteOption" ),
    path('deleteInscription<str:id>/', deleteInscription, name="deleteInscription"),
    path('deletePaiement<str:id>/', deletePaiement, name="deletePaiement"),
    path('deleteClasse<str:id>/', deleteClasse, name="deleteClasse"),
    path('deleteUser<str:id>/', deleteUser, name="deleteUser"),
    path('deleteEleve<str:id>/', deleteEleve, name="deleteEleve"),
    path('deleteFrais<str:id>/', deleteFrais, name="deleteFrais"),
    path('modifierSection<str:id>/', modifierSection, name="modifierSection"),
    path('updateSection<str:id>/', updateSection, name="updateSection"),
    path('modifierOption<str:id>/', modifierOption, name="modifierOption"),
    path('updateOption<str:id>/', updateOption, name="updateOption"),
    path('updateClasse<str:id>/', updateClasse, name="updateClasse"),
    path('modifierClasse<str:id>/', modifierClasse, name="modifierClasse"),
    path('modifierInscription<str:id>/', modifierInscription, name="modifierInscription"),
    path('updateInscription<str:id>/', updateInscription, name="updateInscription"),
    path('modifierEleve<str:id>/', modifierEleve, name="modifierEleve"),
    path('updateEleve<str:id>/', updateEleve, name="updateEleve"),
    path('modifierPaiemet<str:id>/', modifierPaiement, name="modifierPaiement"),
    path('updatePaiement<str:id>/', updatePaiement, name="updatePaiement"),
    path('modifierFrais<str:id>/', modifierFrais, name="modifierFrais"),
    path('updateFrais<str:id>/', updateFrais, name="updateFrais"),
    
    path('sectioninfo/<str:id>', Sectioninfo.as_view(), name="sectioninfo"),
    path('sectiondetails/', SectionDetails, name="sectiondetails"),
    path('sectiondetails/', SectionDetails, name="sectiondetails"),
    path('log_out/', log_out, name="log_out"),
    path('rapportsec/', rapportsec, name="rapportsec"),
    path('rapportopt/', rapportopt, name="rapportopt"),
    path('rapportcla/', rapportcla, name="rapportcla"),
    path('rapportins/', rapportins, name="rapportins"),
    path('rapportele/', rapportele, name="rapportele"),
    path('rapportpai/', rapportpai, name="rapportpai"),
    path('rapportfra/', rapportfra, name="rapportfra"),
    
    
    


]
