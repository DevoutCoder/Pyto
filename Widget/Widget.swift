//
//  Widget.swift
//  Widget
//
//  Created by Adrian Labbé on 25-06-20.
//  Copyright © 2020 Adrian Labbé. All rights reserved.
//

import WidgetKit
import SwiftUI
import Intents

#if WIDGET

<<<<<<< HEAD
=======
// We recycle same scripts used with different layouts
// Key: The bookmark data of the script
// Value: The first Widget ID associated witht the script. Will be reused if the same script is assigned to multiple widgets.
fileprivate var executedWidgets = [Data:String]()

>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
let scriptsQueue = DispatchQueue.global()

var runningScript = false

<<<<<<< HEAD
var widgetsQueue = 0

var ids = [String:String]()

var executingScripts = [String]()

var widgetsToBeReloaded: [String]?

=======
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
struct Provider: IntentTimelineProvider {
    
    typealias Intent = ScriptIntent
    
    typealias Entry = ScriptEntry
    
    func getSnapshot(for configuration: ScriptIntent, in context: Context, completion: @escaping (ScriptEntry) -> Void) {
<<<<<<< HEAD
        var entry = ScriptEntry(date: Date(), output: "")
=======
        var entry = ScriptEntry(date: Date(), output: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non consectetur neque. Morbi faucibus faucibus luctus. Proin porttitor ligula ut justo bibendum molestie. Duis porttitor, eros at viverra aliquet, diam tellus dignissim erat, in pharetra dolor mi at est.", snapshots: [:])
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
        entry.isPlaceholder = true
        completion(entry)
    }
    
    func placeholder(in context: Context) -> ScriptEntry {
        return ScriptEntry(date: Date(), output: NSLocalizedString("noSelectedScript", comment: ""))
    }
    
    func getTimeline(for configuration: ScriptIntent, in context: Context, completion: @escaping (Timeline<ScriptEntry>) -> Void) {
<<<<<<< HEAD
        
        if let toBeReloaded = RuntimeCommunicator.shared.widgetsToBeReloaded {
            widgetsToBeReloaded = toBeReloaded
            RuntimeCommunicator.shared.widgetsToBeReloaded = nil
        }
        
        if configuration.script != nil {
            
            if let toBeReloaded = widgetsToBeReloaded {
                if let filename = configuration.script?.filename, !toBeReloaded.contains(filename) {
                    return
                }
            }
            
            guard let bookmarkData = configuration.script?.data else {
                return completion(Timeline(entries: [], policy: .never))
            }
            
            let name = configuration.script?.filename ?? ""
            
            let id = ids[name] ?? UUID().uuidString
            ids[name] = id
                        
            do {
                var isStale = false
                let url = try URL(resolvingBookmarkData: bookmarkData, bookmarkDataIsStale: &isStale)
                _ = url.startAccessingSecurityScopedResource()
                
                let data = try Data(contentsOf: url)
                var script = try JSONDecoder().decode(IntentScript.self, from: data)
                script.widgetID = id
                
                let scriptURL: URL
                var dir: URL
                let scriptCode: String
                var realPath: String!
                var originalScriptURL: URL?
                do {
                    originalScriptURL = try URL(resolvingBookmarkData: script.bookmarkData, bookmarkDataIsStale: &isStale)
                    _ = originalScriptURL!.startAccessingSecurityScopedResource()
                    dir = directory(for: originalScriptURL!)
                    scriptCode = try String(contentsOf: originalScriptURL!)
                    realPath = originalScriptURL!.path
                } catch {
                    dir = FileManager.default.urls(for: .documentDirectory, in: .allDomainsMask)[0]
                    scriptCode = script.code
                }
                
                scriptURL = FileManager.default.urls(for: .documentDirectory, in: .allDomainsMask)[0].appendingPathComponent("\(id).py")
                let path = scriptURL.path
                if realPath == nil {
                    realPath = path
                }
                
                try scriptCode.write(toFile: path, atomically: true, encoding: .utf8)
                                    
                let code = """
                import widgets
                import sys
                import io
                import os
                from pyto import __Class__
                from outputredirector import Reader
                from time import sleep
                from pyto import Python
                from threading import Thread

                PyWidget = __Class__("PyWidget")

                console = ""

                def read(text):
                    global console
                    console += text
                    PyWidget.breakpoint(text)
                
                write = read

                standardOutput = Reader(read)
                standardOutput._buffer = io.BufferedWriter(standardOutput)
                standardOutput.buffer.write = write

                standardError = Reader(read)
                standardError._buffer = io.BufferedWriter(standardError)
                standardError.buffer.write = write

                sys.stdout = standardOutput
                sys.stderr = standardError

                widgets.__shown_view__ = False
                widgets.__widget_id__ = \"\(id)\"

                PyWidget.breakpoint("Will run")

                class ScriptThread(Thread):
                    script_path = None

                exc = None

                def run(path):
                    global exc
                    import runpy
                    try:
                        runpy.run_path(path)
                    except Exception as e:
                        exc = e

                try:
                    path = "\(path.replacingOccurrences(of: "\"", with: "\\\""))"
                    dir = "\(dir.path.replacingOccurrences(of: "\"", with: "\\\""))"
                    real_path = "\(realPath.replacingOccurrences(of: "\"", with: "\\\""))"
                    os.chdir(dir)
                    if dir not in sys.path:
                        sys.path.append(dir)

                    thread = ScriptThread(target=run, args=(str(path),))
                    thread.script_path = str(real_path)
                    thread.start()
                    thread.join()

                    if exc is not None:
                        raise exc
                except Exception as e:
                    console += str(e)+"\\n"

                PyWidget.breakpoint("Doneeee")

                if not widgets.__shown_view__:
                    widget = PyWidget.alloc().init()
                    
                    if console.endswith("\\n"):
                        console = console[:-1]

                    widget.output = console
                    PyWidget.updateTimeline(\"\(id)\", widget=widget)
                """
                                    
                url.stopAccessingSecurityScopedResource()
                                    
                if PyWidget.makeTimeline[id] == nil {
                    PyWidget.makeTimeline[id] = []
                }
                
                var list = PyWidget.makeTimeline[id]
                list?.append(completion)
                PyWidget.makeTimeline[id] = list

                func run() {
                    runningScript = true
                    PyWidget.widgetCode = script.code
                    scriptsQueue.async {
                        
                        func clear() {
                            widgetsQueue -= 1
                            if let i = executingScripts.firstIndex(of: name) {
                                executingScripts.remove(at: i)
                            }
                            ProcessInfo.processInfo.performExpiringActivity(withReason: "Because I want to") { (expired) in
                                
                                if !expired {
                                    Thread.sleep(forTimeInterval: 3)
                                }
                                
                                if widgetsQueue <= 0 {
                                    exit(0)
                                }
                            }
                        }
                        
                        if RuntimeCommunicator.shared.isContainerAppRunning {
                            RuntimeCommunicator.shared.runScript(entry: script) { (entry) in
                                runningScript = false
                                
                                let date = Date().addingTimeInterval(entry.updateInterval ?? 0)
                                completion(Timeline(entries: [entry], policy: .after(date)))
                                
                                clear()
                            }
                        } else {
=======
        if configuration.script != nil {
            let id = UUID().uuidString
            
            guard let bookmarkData = configuration.script?.data else {
                return
            }
            
            do {
                if executedWidgets[bookmarkData] == nil {
                    var isStale = false
                    let url = try URL(resolvingBookmarkData: bookmarkData, bookmarkDataIsStale: &isStale)
                    _ = url.startAccessingSecurityScopedResource()
                    
                    let data = try Data(contentsOf: url)
                    let script = try JSONDecoder().decode(IntentScript.self, from: data)
                    
                    let scriptURL: URL
                    var dir: URL
                    let scriptCode: String
                    var realPath: String!
                    var originalScriptURL: URL?
                    do {
                        originalScriptURL = try URL(resolvingBookmarkData: script.bookmarkData, bookmarkDataIsStale: &isStale)
                        _ = originalScriptURL!.startAccessingSecurityScopedResource()
                        dir = directory(for: originalScriptURL!)
                        scriptCode = try String(contentsOf: originalScriptURL!)
                        realPath = originalScriptURL!.path
                    } catch {
                        dir = FileManager.default.urls(for: .documentDirectory, in: .allDomainsMask)[0]
                        scriptCode = script.code
                    }
                    
                    scriptURL = FileManager.default.urls(for: .documentDirectory, in: .allDomainsMask)[0].appendingPathComponent("\(id).py")
                    let path = scriptURL.path
                    if realPath == nil {
                        realPath = path
                    }
                    
                    try scriptCode.write(toFile: path, atomically: true, encoding: .utf8)
                    
                    executedWidgets[bookmarkData] = id
                    
                    let code = """
                    import widgets
                    import sys
                    import io
                    import os
                    from pyto import __Class__
                    from outputredirector import Reader
                    from time import sleep
                    from pyto import Python
                    from threading import Thread

                    PyWidget = __Class__("PyWidget")

                    console = ""

                    def read(text):
                        global console
                        console += text
                        PyWidget.breakpoint(text)
                    
                    write = read

                    standardOutput = Reader(read)
                    standardOutput._buffer = io.BufferedWriter(standardOutput)
                    standardOutput.buffer.write = write

                    standardError = Reader(read)
                    standardError._buffer = io.BufferedWriter(standardError)
                    standardError.buffer.write = write

                    sys.stdout = standardOutput
                    sys.stderr = standardError

                    widgets.__shown_view__ = False
                    widgets.__widget_id__ = \"\(id)\"

                    PyWidget.breakpoint("Will run")

                    class ScriptThread(Thread):
                        script_path = None

                    exc = None

                    def run(path):
                        global exc
                        import runpy
                        try:
                            runpy.run_path(path)
                        except Exception as e:
                            exc = e

                    try:
                        path = "\(path.replacingOccurrences(of: "\"", with: "\\\""))"
                        dir = "\(dir.path.replacingOccurrences(of: "\"", with: "\\\""))"
                        real_path = "\(realPath.replacingOccurrences(of: "\"", with: "\\\""))"
                        os.chdir(dir)
                        if dir not in sys.path:
                            sys.path.append(dir)

                        thread = ScriptThread(target=run, args=(str(path),))
                        thread.script_path = str(real_path)
                        thread.start()
                        thread.join()

                        if exc is not None:
                            raise exc
                    except Exception as e:
                        console += str(e)+"\\n"

                    PyWidget.breakpoint("Doneeee")

                    if not widgets.__shown_view__:
                        widget = PyWidget.alloc().init()
                        
                        if console.endswith("\\n"):
                            console = console[:-1]

                        widget.output = console
                        PyWidget.updateTimeline(\"\(id)\", widget=widget)
                    """
                                        
                    url.stopAccessingSecurityScopedResource()
                    
                    SetupPython()
                    
                    if PyWidget.makeTimeline[id] == nil {
                        PyWidget.makeTimeline[id] = []
                    }
                    
                    var list = PyWidget.makeTimeline[id]
                    list?.append(completion)
                    PyWidget.makeTimeline[id] = list
                    
                    func run() {
                        runningScript = true
                        PyWidget.widgetCode = script.code
                        scriptsQueue.async {
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
                            Python.pythonShared?.perform(#selector(PythonRuntime.runWidgetWithCode(_:andID:)), with: code, with: id)
                            runningScript = false
                            try? FileManager.default.removeItem(at: scriptURL)
                            originalScriptURL?.stopAccessingSecurityScopedResource()
                            dir.stopAccessingSecurityScopedResource()
<<<<<<< HEAD
                            
                            clear()
                        }
                    }
                }
                
                if !executingScripts.contains(name) {
                    executingScripts.append(name)
                    widgetsQueue += 1
                    
                    if !RuntimeCommunicator.shared.isContainerAppRunning && !Python.shared.isSetup {
                        SetupPython()
                    }
                    
                    if (Python.shared.isSetup || RuntimeCommunicator.shared.isContainerAppRunning) && !runningScript {
                        run()
                    } else {
                        _ = Timer.scheduledTimer(withTimeInterval: 0.01, repeats: true, block: { (timer) in
                            if (Python.shared.isSetup || RuntimeCommunicator.shared.isContainerAppRunning) && !runningScript {
=======
                        }
                    }
                    
                    if Python.shared.isSetup && !runningScript {
                        run()
                    } else {
                        _ = Timer.scheduledTimer(withTimeInterval: 0.2, repeats: true, block: { (timer) in
                            if Python.shared.isSetup && !runningScript {
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
                                run()
                                timer.invalidate()
                            }
                        })
                    }
<<<<<<< HEAD
                }
            } catch {
                print(error.localizedDescription)
                completion(Timeline(entries: [], policy: .never))
=======
                } else if let id = executedWidgets[bookmarkData] {
                    if let timeline = PyWidget.timelines[id] {
                        completion(timeline)
                    } else {
                        var list = PyWidget.makeTimeline[id]
                        list?.append(completion)
                        PyWidget.makeTimeline[id] = list
                    }
                }
                
            } catch {
                print(error.localizedDescription)
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
            }
        } else {
            completion(Timeline(entries: [ScriptEntry(date: Date(), output: NSLocalizedString("noSelectedScript", comment: ""))], policy: .never))
        }
    }
}

<<<<<<< HEAD
struct InAppProvider: IntentTimelineProvider {    
=======
struct InAppProvider: IntentTimelineProvider {
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
    
    typealias Intent = SetContentInAppIntent
    
    typealias Entry = ScriptEntry
    
    func getSnapshot(for configuration: SetContentInAppIntent, in context: Context, completion: @escaping (ScriptEntry) -> Void) {
<<<<<<< HEAD
        var entry = ScriptEntry(date: Date(), output: "")
        entry.isPlaceholder = true
        entry.inApp = true
=======
        var entry = ScriptEntry(date: Date(), output: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non consectetur neque. Morbi faucibus faucibus luctus. Proin porttitor ligula ut justo bibendum molestie. Duis porttitor, eros at viverra aliquet, diam tellus dignissim erat, in pharetra dolor mi at est.", snapshots: [:])
        entry.isPlaceholder = true
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
        completion(entry)
    }
    
    func placeholder(in context: Context) -> ScriptEntry {
        return ScriptEntry(date: Date(), output: NSLocalizedString("noSelectedScript", comment: ""))
    }
    
    func getTimeline(for configuration: SetContentInAppIntent, in context: Context, completion: @escaping (Timeline<ScriptEntry>) -> Void) {
<<<<<<< HEAD
                
        if let category = configuration.category {
            guard let entry = InAppWidgetsStore.shared.get(category.identifier ?? "") else {
                return completion(Timeline(entries: [], policy: .never))
            }
            completion(Timeline(entries: [entry], policy: .never))
=======
        if let category = configuration.category {
            
            let saved = UserDefaults.shared?.value(forKey: "savedWidgets") as? [String:Data]
            
            guard let data = saved?[category.identifier ?? ""] else {
                return
            }
            
            do {
                let entry = try JSONDecoder().decode(ScriptEntry.self, from: data)
                completion(Timeline(entries: [entry], policy: .never))
            } catch {
                print(error.localizedDescription)
            }
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
        } else {
            completion(Timeline(entries: [ScriptEntry(date: Date(), output: NSLocalizedString("noSelectedScript", comment: ""))], policy: .never))
        }
    }
}
#endif

<<<<<<< HEAD
let backgroundGradient = LinearGradient(gradient: Gradient(colors: [Color(red: 0/255, green: 242/255, blue: 44/255), Color(red: 8/255, green: 214/255, blue: 87/255)]), startPoint: .top, endPoint: .bottom)

=======
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
@available(iOS 14.0, *)
struct WidgetEntryView : View {
    
    @Environment(\.widgetFamily) var family
<<<<<<< HEAD
    
=======
        
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
    var entry: ScriptEntry
        
    var customFamily: WidgetFamily?
    
    init(entry: ScriptEntry, customFamily: WidgetFamily? = nil) {
        self.entry = entry
        self.customFamily = customFamily
    }
    
    var body: some View {
        
<<<<<<< HEAD
        if entry.isPlaceholder {
            return AnyView(PlaceholderView(inApp: entry.inApp))
        } else {
            let family = customFamily ?? self.family
            
            if let view = entry.view?[family] {
                view.entry = entry
                let widgetView = view.makeView
                var background = view.backgroundImage?.makeView ?? AnyView(Color(view.backgroundColor ?? UIColor.systemBackground))
                let url = entry.url(viewID: view.link)
                
                if let gradient = view.backgroundGradient {
                    var gradientColors = [Color]()
                    for color in gradient {
                        gradientColors.append(Color(color))
                    }
                    background = AnyView(LinearGradient(gradient: Gradient(colors: gradientColors), startPoint: .top, endPoint: .bottom))
                }
                            
                if family == .systemMedium {
                    #if WIDGET
                    return AnyView(ZStack {
                        background
                        widgetView
                    }.widgetURL(url))
                    #else
                    return AnyView(ZStack {
                        background
                        widgetView/*.padding(.vertical)*/
                    }.widgetURL(url))
                    #endif
                } else {
                    return AnyView(ZStack {
                        background
                        widgetView/*.padding()*/
                    }.widgetURL(url))
                }
            } else {
                
                let view = HStack { () -> AnyView in
                    if let snapshot = entry.snapshots[family] {
                        return AnyView(Image(uiImage: snapshot.0).resizable().scaledToFill())
                    } else {
                        var text = AnyView(Text(entry.output).foregroundColor(.black).font(.headline))
                        if entry.isPlaceholder {
                            text = AnyView(text.redacted(reason: .placeholder))
                        }
                        return AnyView(text.padding())
                    }
                }
                
                return AnyView(ZStack {
                    if let color = entry.snapshots[family]?.1 {
                        Color(color)
                    } else {
                        backgroundGradient
                    }
                    
                    view
                }.overlay(VStack {
                    if entry.output == NSLocalizedString("noSelectedScript", comment: "") {
                        HStack {
                            Image(systemName: "exclamationmark.triangle").foregroundColor(.black).padding(10)
                            Spacer()
                        }
                        Spacer()
                    }
                }))
            }
        }
    }
}

@available(iOS 14.0, *)
struct PlaceholderView: View {
    
    var inApp: Bool
    
    var body: some View {
        ZStack {
            backgroundGradient
            
            Image(systemName: inApp ? "app.badge.fill" : "play.fill")
                .font(.system(size: 80))
                .foregroundColor(.black)
=======
        let family = customFamily ?? self.family
        
        if let view = entry.view?[family] {
            view.entry = entry
            let widgetView = view.makeView
            let background = view.backgroundImage?.makeView ?? AnyView(Color(view.backgroundColor ?? UIColor.systemBackground))
            let url = entry.url(viewID: view.link)
                        
            if family == .systemMedium {
                #if WIDGET
                return AnyView(ZStack {
                    background
                    widgetView
                }.widgetURL(url))
                #else
                return AnyView(ZStack {
                    background
                    widgetView/*.padding(.vertical)*/
                }.widgetURL(url))
                #endif
            } else {
                return AnyView(ZStack {
                    background
                    widgetView/*.padding()*/
                }.widgetURL(url))
            }
        } else {
            
            return AnyView(HStack { () -> AnyView in
                if let snapshot = entry.snapshots[family] {
                    return AnyView(Image(uiImage: snapshot.0).resizable().scaledToFill())
                } else {
                    var text = AnyView(Text(entry.output))
                    if entry.isPlaceholder {
                        text = AnyView(text.redacted(reason: .placeholder))
                    }
                    return AnyView(text.padding())
                }
            }.padding().background(Color(entry.snapshots[family]?.1 ?? UIColor.clear)))
>>>>>>> 9ec484051b222280c44a9356f1eb31cfa9a71619
        }
    }
}

#if WIDGET

struct RunScriptWidget: Widget {
    private let kind: String = "Script"

    public var body: some WidgetConfiguration {
        IntentConfiguration(kind: kind, intent: ScriptIntent.self, provider: Provider(), content: { entry in
            WidgetEntryView(entry: entry)
        })
        .configurationDisplayName("runScript")
        .description("widgetDescriptionRunScript")
    }
}

struct SetContentInAppWidget: Widget {
    private let kind: String = "SetInApp"

    public var body: some WidgetConfiguration {
        IntentConfiguration(kind: kind, intent: SetContentInAppIntent.self, provider: InAppProvider(), content: { entry in
            WidgetEntryView(entry: entry)
        })
        .configurationDisplayName("In App")
        .description("widgetDescriptionInApp")
    }
}

@main
struct PytoWidgets: WidgetBundle {
    
    @WidgetBundleBuilder
    var body: some Widget {
        RunScriptWidget()
        SetContentInAppWidget()
    }
}
#endif
