import os

vaultfilenames = set(('40050_2421406273_0406-02147.jpg','allenc.jpg','andrews01a.jpg','andrewsPlaque.jpg','andrews athletic.jpg','armstrong.jpg','Ashford, Paul (Photo).jpg','auman.jpg','Bagale, John (Photo).jpg','Baker, Baxter (Photo).jpg','Ballard.png','Barnes Jr..png','barnwell.jpg','beattycg.jpg','behrman.jpg','benfield.jpg','bishope.jpg','blackwld.jpg','boseman.jpg','bost.jpg','Boukedes, Christos (Photo).jpg','bowman.jpg','boycef.jpg','boyd.jpg','Bradley Jr..png','brooksal.jpg','brown.jpg','browning.jpg','brownw.jpg','brownwe.jpg','burke.jpg','burnham.jpg','burns.jpg','byars.jpg','byrd.jpg','byrumc.jpg','Callahan.png','campbell.jpg','carney.jpg','carson.jpg','carter.jpg','cassels.jpg','cavert.jpg','clarkt.jpg','clemmons.jpg','Correll, Daniel (Photo).jpg','covington.jpg','coyle.jpg','crabb.jpg','cranford.jpg','crowell.jpg','culbreth.jpg','dabney.jpg','dailey.jpg','Davis D..png','Davis Jr..png','davis.jpg','Dawkins, Williw (Photo).jpg','dawson.jpg','dealf.jpg','DeArmon, Charles (Photo).jpg','deaser.jpg','deberry.jpg','doar.jpg','Dulin, James (Photo).jpg','dumas.jpg','Edwards.png','fairell.jpg','fidler.jpg','finlayt.jpg','fogg.jpg','forbes.jpg','forbis.jpg','fordrlph.jpg','fordwalt.jpg','foscue.jpg','fowler.jpg','foxlaw.jpg','fraley.jpg','frederick.jpg','fulbrigt.jpg','fulcher.jpg','furrart.jpg','gallaghr.jpg','gant.jpg','gantt.jpg','gardner.jpg','garrh.jpg','garrison.jpg','garrou.jpg','gibson.jpg','Gold.png','gordon.jpg','graham.jpg','gray.jpg','grayl.jpg','greene.jpg','Greene.png','greenm.jpg','greenway.jpg','gregory.jpg','griffine.jpg','griffinm.jpg','griffite.jpg','grifithc.jpg','grifithm.jpg','grimes.jpg','GSV001.png','GSV002.jpg','GSV003.jpg','GSV004.jpg','GSV005a.jpg','GSV006.png','GSV008a.jpg','GSV009a.jpg','GSV012.jpg','GSV013.jpg','GSV015.jpg','GSV016.jpg','GSV017.jpg','GSV018.jpg','GSV019.jpg','GSV021.jpg','GSV023.jpg','GSV025a.jpg','GSV031.jpg','GSV032.jpg','GSV033.jpg','GSV034.jpg','GSV035.jpg','GSV036.jpg','GSV037.jpg','GSV038.jpg','GSV039.jpg','GSV040.jpg','GSV042.jpg','GSV044.jpg','GSV045.jpg','GSV046.jpg','GSV047.jpg','GSV052.jpg','GSV057.jpg','GSV058.jpg','GSV059.jpg','GSV064.jpg','GSV065.jpg','GSV066.jpg','GSV067.jpg','GSV068.jpg','GSV074.jpg','GSV075.jpg','GSV076.jpg','GSV079.jpg','GSV080.jpg','GSV081.jpg','GSV082.jpg','GSV083.jpg','GSV084.jpg','GSV089.jpg','GSV090.jpg','GSV091.jpg','GSV092.jpg','GSV093.jpg','GSV095.jpg','GSV096.jpg','GSV098.jpg','GSV101.jpg','GSV102.jpg','GSV104.jpg','GSV107.jpg','GSV109.jpg','GSV116.jpg','GSV117.jpg','GSV118.jpg','GSV120.jpg','GSV122.jpg','GSV125.jpg','GSV132.jpg','GSV134.jpg','GSV135.jpg','GSV136.jpg','GSV137.jpg','GSV138.jpg','GSV139.jpg','GSV142.jpg','GSV143.jpg','GSV144.jpg','GSV145.jpg','GSV146.jpg','GSV147.jpg','GSV148.jpg','GSV149.jpg','GSV150.jpg','GSV152.jpg','GSV157.jpg','GSV160.jpg','GSV163.jpg','GSV165.jpg','GSV166.jpg','GSV167.jpg','GSV172.jpg','GSV173.jpg','GSV175.jpg','GSV176.jpg','GSV177.jpg','GSV180.jpg','GSV181.jpg','GSV182.jpg','GSV183.jpg','GSV184.jpg','GSV185.jpg','GSV186.jpg','GSV187.jpg','GSV188.jpg','GSV194.jpg','GSV195.jpg','GSV196.jpg','GSV197.jpg','GSV200.jpg','GSV201.jpg','GSV202.jpg','GSV203.jpg','GSV204.jpg','GSV205.jpg','GSV206.jpg','GSV207.jpg','GSV208.jpg','GSV210.jpg','GSV212.jpg','gunthorp.jpg','gurley.jpg','hackney.jpg','hagan.jpg','hager.jpg','haigler.jpg','haiglerh.jpg','hall.jpg','hammond.jpg','hancockj.jpg','harden.jpg','hargett.jpg','harman.jpg','harnsberger.jpg','Harrill.png','harrisj.jpg','harrison.jpg','hart.jpg','hartzog.jpg','hattrich.jpg','hay.jpg','hayes.jpg','heath.jpg','hedrick.jpg','hedrickl.jpg','Hegwood.png','heins.jpg','helms.jpg','helmsa.jpg','helmsf.jpg','helmsl.jpg','hendrix.jpg','henleyc.jpg','henning.jpg','henry.jpg','herman.jpg','hicks.jpg','hill.jpg','Hodges.png','hoffman.jpg','holder.jpg','holt.jpg','holton.jpg','hoover.jpg','horton.jpg','hovis.jpg','hunnicut.jpg','hunter.jpg','ingramj.jpg','iverson.jpg','ivery.jpg','ivey_0.jpg','jackson_0.jpg','jacksona.jpg','jamesa.jpg','jamesj.jpg','jamesr.jpg','jeffersn.jpg','Johnson.png','johnston.jpg','jonesm.jpg','jonesw.jpg','jordan.jpg','joyner.jpg','keerans.jpg','kirkley.jpg','knapp.jpg','knotts.jpg','knowles.jpg','knoxa.jpg','knoxw.jpg','kurtz.jpg','lackey.jpg','lambe.jpg','latimer.jpg','lawhon.jpg','lawing.jpg','Lawing.png','lawrence.jpg','lawther.jpg','lee.jpg','leonhard.jpg','littleg.jpg','Lloyd.png','longwp.jpg','lothrey.jpg','lovej.jpg','lowrance.jpg','lundy.jpg','lytch.jpg','marshall.jpg','mcallister.jpg','mcalpine.jpg','mccain.jpg','mccallum.jpg','mcclella.jpg','mcclintic.jpg','mccraw.jpg','mcginnis.jpg','mckinney.jpg','mckinney2.jpg','mckinnon.jpg','mcleod.jpg','mcneely.jpg','melton.jpg','menzies.jpg','mewborne.jpg','mickle.jpg','middleto.jpg','millerf.jpg','millerj.jpg','Mills, John (Photo).jpg','mntgmry.jpg','moore.jpg','moorer.jpg','morehous.jpg','morgan.jpg','morganc.jpg','morrisd.jpg','morton.jpg','Moses.png','mostelle.jpg','mueller.jpg','munday.jpg','myers_0.jpg','Nance.png','newbold.jpg','nichols.jpg','nicholson.jpg','niven.jpg','noelj.jpg','norton.jpg','osbornej.jpg','osbornm.jpg','otto.jpg','overcash.jpg','owens.jpg','parkerj.jpg','parkerr.jpg','patton.jpg','pearsall.jpg','pegram.jpg','peninger.jpg','pennington.jpg','peoples2.jpg','Pettit.png','phifer.jpg','philbeck.jpg','phillips.jpg','pierce.jpg','pittman.jpg','plyler.jpg','plylerf.jpg','poovey.jpg','pope.jpg','Powell, Donald (Photo).jpg','price.jpg','pricew.jpg','pritchrd.jpg','quarles.jpg','raley.jpg','RandolphParis01.jpg','RandolphParis02.jpg','rape.jpg','rayburn.jpg','Richardson, Amos (Photo).jpg','riddle.jpg','ritch.jpg','ritter.jpg','robertson.jpg','royster.jpg','scarbrgh.jpg','schaeffr.jpg','schiltz.jpg','schneidt.jpg','scottn.jpg','sellers.jpg','shamburg.jpg','sharp.jpg','shaw.jpg','sheathlm.jpg','Shellnutt, John (Photo).jpg','shirah.jpg','simmons.jpg','smithb.jpg','smithd.jpg','somervell.jpg','Stansell.png','Starkey, Clyde (Photo).jpg','starnes.jpg','Starnes.png','stewart.jpg','stuart.jpg','Sullivan.png','Sutton.png','suttonhl.jpg','taliaferro.jpg','terry.jpg','tharp.jpg','thomasb.jpg','tipton.jpg','towill.jpg','tuckerw.jpg','turner.jpg','turner_0.jpg','turnerwt.jpg','Wade Jr..png','ward.jpg','washburn.jpg','Watts, Roy (Photo).jpg','wheeler.jpg','whitesd.jpg','wickerm.jpg','willimsd.jpg','willimsh.jpg','willimsr.jpg','wilson.jpg','wilsongf.jpg','wilsonhm.jpg','wilsonl.jpg','withers.jpg','wolfe.jpg','wooten.jpg','ww2placeholder.gif','ww2placeholder_0.gif','ww2placeholder_1.gif','ww2placeholder_10.gif','ww2placeholder_100.gif','ww2placeholder_101.gif','ww2placeholder_102.gif','ww2placeholder_103.gif','ww2placeholder_104.gif','ww2placeholder_105.gif','ww2placeholder_106.gif','ww2placeholder_107.gif','ww2placeholder_108.gif','ww2placeholder_109.gif','ww2placeholder_110.gif','ww2placeholder_111.gif','ww2placeholder_112.gif','ww2placeholder_113.gif','ww2placeholder_114.gif','ww2placeholder_115.gif','ww2placeholder_116.gif','ww2placeholder_117.gif','ww2placeholder_118.gif','ww2placeholder_119.gif','ww2placeholder_12.gif','ww2placeholder_120.gif','ww2placeholder_121.gif','ww2placeholder_122.gif','ww2placeholder_123.gif','ww2placeholder_124.gif','ww2placeholder_125.gif','ww2placeholder_126.gif','ww2placeholder_127.gif','ww2placeholder_128.gif','ww2placeholder_129.gif','ww2placeholder_13.gif','ww2placeholder_130.gif','ww2placeholder_131.gif','ww2placeholder_132.gif','ww2placeholder_133.gif','ww2placeholder_134.gif','ww2placeholder_135.gif','ww2placeholder_136.gif','ww2placeholder_137.gif','ww2placeholder_138.gif','ww2placeholder_139.gif','ww2placeholder_14.gif','ww2placeholder_140.gif','ww2placeholder_141.gif','ww2placeholder_142.gif','ww2placeholder_143.gif','ww2placeholder_144.gif','ww2placeholder_145.gif','ww2placeholder_146.gif','ww2placeholder_147.gif','ww2placeholder_148.gif','ww2placeholder_149.gif','ww2placeholder_15.gif','ww2placeholder_150.gif','ww2placeholder_151.gif','ww2placeholder_152.gif','ww2placeholder_153.gif','ww2placeholder_154.gif','ww2placeholder_155.gif','ww2placeholder_156.gif','ww2placeholder_157.gif','ww2placeholder_158.gif','ww2placeholder_159.gif','ww2placeholder_16.gif','ww2placeholder_160.gif','ww2placeholder_161.gif','ww2placeholder_162.gif','ww2placeholder_163.gif','ww2placeholder_164.gif','ww2placeholder_165.gif','ww2placeholder_166.gif','ww2placeholder_167.gif','ww2placeholder_168.gif','ww2placeholder_169.gif','ww2placeholder_17.gif','ww2placeholder_170.gif','ww2placeholder_171.gif','ww2placeholder_172.gif','ww2placeholder_173.gif','ww2placeholder_174.gif','ww2placeholder_175.gif','ww2placeholder_176.gif','ww2placeholder_177.gif','ww2placeholder_178.gif','ww2placeholder_179.gif','ww2placeholder_18.gif','ww2placeholder_180.gif','ww2placeholder_181.gif','ww2placeholder_182.gif','ww2placeholder_183.gif','ww2placeholder_184.gif','ww2placeholder_185.gif','ww2placeholder_186.gif','ww2placeholder_187.gif','ww2placeholder_188.gif','ww2placeholder_189.gif','ww2placeholder_19.gif','ww2placeholder_190.gif','ww2placeholder_191.gif','ww2placeholder_192.gif','ww2placeholder_193.gif','ww2placeholder_194.gif','ww2placeholder_195.gif','ww2placeholder_196.gif','ww2placeholder_197.gif','ww2placeholder_198.gif','ww2placeholder_199.gif','ww2placeholder_2.gif','ww2placeholder_20.gif','ww2placeholder_200.gif','ww2placeholder_201.gif','ww2placeholder_202.gif','ww2placeholder_203.gif','ww2placeholder_204.gif','ww2placeholder_205.gif','ww2placeholder_206.gif','ww2placeholder_207.gif','ww2placeholder_208.gif','ww2placeholder_209.gif','ww2placeholder_21.gif','ww2placeholder_210.gif','ww2placeholder_211.gif','ww2placeholder_212.gif','ww2placeholder_213.gif','ww2placeholder_214.gif','ww2placeholder_215.gif','ww2placeholder_216.gif','ww2placeholder_217.gif','ww2placeholder_218.gif','ww2placeholder_219.gif','ww2placeholder_22.gif','ww2placeholder_220.gif','ww2placeholder_221.gif','ww2placeholder_222.gif','ww2placeholder_223.gif','ww2placeholder_224.gif','ww2placeholder_225.gif','ww2placeholder_226.gif','ww2placeholder_227.gif','ww2placeholder_228.gif','ww2placeholder_229.gif','ww2placeholder_23.gif','ww2placeholder_230.gif','ww2placeholder_231.gif','ww2placeholder_232.gif','ww2placeholder_233.gif','ww2placeholder_234.gif','ww2placeholder_235.gif','ww2placeholder_236.gif','ww2placeholder_237.gif','ww2placeholder_238.gif','ww2placeholder_239.gif','ww2placeholder_24.gif','ww2placeholder_240.gif','ww2placeholder_241.gif','ww2placeholder_242.gif','ww2placeholder_243.gif','ww2placeholder_244.gif','ww2placeholder_245.gif','ww2placeholder_246.gif','ww2placeholder_247.gif','ww2placeholder_248.gif','ww2placeholder_249.gif','ww2placeholder_25.gif','ww2placeholder_250.gif','ww2placeholder_251.gif','ww2placeholder_252.gif','ww2placeholder_253.gif','ww2placeholder_254.gif','ww2placeholder_255.gif','ww2placeholder_26.gif','ww2placeholder_27.gif','ww2placeholder_28.gif','ww2placeholder_29.gif','ww2placeholder_3.gif','ww2placeholder_30.gif','ww2placeholder_31.gif','ww2placeholder_32.gif','ww2placeholder_33.gif','ww2placeholder_34.gif','ww2placeholder_35.gif','ww2placeholder_36.gif','ww2placeholder_37.gif','ww2placeholder_38.gif','ww2placeholder_39.gif','ww2placeholder_4.gif','ww2placeholder_40.gif','ww2placeholder_41.gif','ww2placeholder_42.gif','ww2placeholder_43.gif','ww2placeholder_44.gif','ww2placeholder_45.gif','ww2placeholder_46.gif','ww2placeholder_47.gif','ww2placeholder_48.gif','ww2placeholder_49.gif','ww2placeholder_5.gif','ww2placeholder_50.gif','ww2placeholder_51.gif','ww2placeholder_52.gif','ww2placeholder_53.gif','ww2placeholder_54.gif','ww2placeholder_55.gif','ww2placeholder_56.gif','ww2placeholder_57.gif','ww2placeholder_58.gif','ww2placeholder_59.gif','ww2placeholder_6.gif','ww2placeholder_60.gif','ww2placeholder_61.gif','ww2placeholder_62.gif','ww2placeholder_63.gif','ww2placeholder_64.gif','ww2placeholder_65.gif','ww2placeholder_66.gif','ww2placeholder_67.gif','ww2placeholder_68.gif','ww2placeholder_69.gif','ww2placeholder_7.gif','ww2placeholder_70.gif','ww2placeholder_71.gif','ww2placeholder_72.gif','ww2placeholder_73.gif','ww2placeholder_74.gif','ww2placeholder_75.gif','ww2placeholder_76.gif','ww2placeholder_77.gif','ww2placeholder_78.gif','ww2placeholder_79.gif','ww2placeholder_8.gif','ww2placeholder_80.gif','ww2placeholder_81.gif','ww2placeholder_82.gif','ww2placeholder_83.gif','ww2placeholder_84.gif','ww2placeholder_85.gif','ww2placeholder_86.gif','ww2placeholder_87.gif','ww2placeholder_88.gif','ww2placeholder_89.gif','ww2placeholder_9.gif','ww2placeholder_90.gif','ww2placeholder_91.gif','ww2placeholder_92.gif','ww2placeholder_93.gif','ww2placeholder_94.gif','ww2placeholder_95.gif','ww2placeholder_96.gif','ww2placeholder_97.gif','ww2placeholder_98.gif','ww2placeholder_99.gif','yarboro.jpg','yelton.jpg'))
cmsDirectory = "C:\\Users\\joconnor\\Desktop\\cmstorycopy"
vaultDirectory = "C:\\Users\\joconnor\\Desktop\\tovault\\"

def cutFiles():
	global vaultfilenames
	global cmsdirfiles
	global vaultdirfiles
	dups = 0
	deleted = 0

	for i in vaultfilenames:
		for root, dirs, files in os.walk(cmsDirectory):
			for f in files:
				if f == i:
					try:
						os.rename(os.path.join(root,f),vaultDirectory+f)
						print("Moved " + i)
					except FileExistsError:
						cmsFileSize = os.path.getsize(os.path.join(root,f))
						vaultFileSize = os.path.getsize(os.path.join(vaultDirectory,f))
						if cmsFileSize > vaultFileSize:
							os.remove(os.path.join(vaultDirectory,f))
							os.rename(os.path.join(root,f),vaultDirectory+f)
							dups = dups+1
							print("Replaced " + f)
						else:
							os.remove(os.path.join(root,f))
							deleted = deleted + 1
							print("Deleted " + f)
				else:
					continue

	print("Replaced " + str(dups) + " total files and deleted " + str(deleted) + " files that were smaller")

cutFiles()
